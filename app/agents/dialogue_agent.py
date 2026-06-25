"""
Dialogue Agent — handles query answering.

Pipeline:
1. Embed the question.
2. Fetch all nodes from Neo4j.
3. Score each node by cosine similarity to the question embedding.
4. Select the top-k nodes as context.
5. Also fetch any CONTRADICTS edges relevant to the context nodes.
6. Send context + question to Groq LLM using the RAG_PROMPT.
7. Return the answer, source node IDs, and any active contradictions.
"""

from app.embeddings.embedder import embedder
from app.embeddings.similarity import SimilarityService
from app.graph.neo4j_client import neo4j_client
from app.llm.groq_client import groq_client
from app.llm.prompts.dialogue_prompts import RAG_PROMPT

TOP_K = 5  # Number of context nodes to retrieve


def _fetch_nodes_with_embeddings() -> list[dict]:
    query = """
    MATCH (n)
    WHERE n.embedding IS NOT NULL
    RETURN n.id AS id, n.text AS text, n.confidence AS confidence, n.embedding AS embedding
    """
    return neo4j_client.execute_query(query)


def _fetch_contradictions(node_ids: list[str]) -> list[dict]:
    """Find any CONTRADICTS edges involving the context nodes."""
    if not node_ids:
        return []
    query = """
    MATCH (a)-[r:CONTRADICTS]->(b)
    WHERE a.id IN $ids OR b.id IN $ids
    RETURN a.text AS node_a, b.text AS node_b, r.weight AS weight
    """
    return neo4j_client.execute_query(query, {"ids": node_ids})


class DialogueAgent:

    @staticmethod
    def answer(question: str, mode: str = "factual") -> dict:
        # 1. Embed the question
        q_embedding = embedder.embed_text(question)

        # 2. Fetch all nodes
        nodes = _fetch_nodes_with_embeddings()

        if not nodes:
            return {
                "answer": "Your knowledge graph is empty. Please ingest some knowledge first.",
                "sources": [],
                "contradictions": []
            }

        # 3. Score and rank nodes
        scored = []
        for node in nodes:
            emb = node.get("embedding")
            if not emb:
                continue
            score = SimilarityService.cosine_similarity(q_embedding, emb)
            scored.append({
                "id": node["id"],
                "text": node["text"],
                "confidence": node.get("confidence", 1.0),
                "score": score
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        top_nodes = scored[:TOP_K]

        # 4. Build context string
        context_parts = []
        for i, node in enumerate(top_nodes, 1):
            conf = node["confidence"] or 1.0
            context_parts.append(
                f"[Node {i} | Confidence: {conf:.2f}]\n{node['text']}"
            )
        context_str = "\n\n---\n\n".join(context_parts)

        # 5. Fetch active contradictions for context nodes
        source_ids = [n["id"] for n in top_nodes]
        contradictions = _fetch_contradictions(source_ids)
        conflict_notes = []
        if contradictions:
            conflict_notes.append("\n\n⚠️ ACTIVE CONTRADICTIONS IN YOUR KNOWLEDGE BASE:")
            for c in contradictions[:3]:
                conflict_notes.append(
                    f"  • \"{c.get('node_a', '')}\" CONTRADICTS \"{c.get('node_b', '')}\""
                )
            context_str += "\n".join(conflict_notes)

        # 6. Build the prompt
        if mode == "socratic":
            from app.llm.prompts.dialogue_prompts import SOCRATIC_PROMPT
            prompt = SOCRATIC_PROMPT.format(
                context=context_str,
                question=question
            )
        else:
            prompt = RAG_PROMPT.format(
                context=context_str,
                question=question
            )

        # 7. Call Groq
        try:
            answer = groq_client.generate(prompt, temperature=0.3)
        except Exception as e:
            answer = f"LLM error: {e}"

        return {
            "answer": answer,
            "sources": source_ids,
            "contradictions": [
                {"a": c.get("node_a", ""), "b": c.get("node_b", "")}
                for c in contradictions
            ]
        }