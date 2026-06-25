"""
Coherence Agent — Phase 2 of the MNEMO ingestion pipeline.

Given a new chunk (text + embedding), it:
1. Fetches all existing nodes from Neo4j (with their embeddings).
2. Computes cosine similarity against each existing node.
3. Picks the most similar existing node (if any above the EMERGE threshold).
4. Sends both texts to Groq LLM with the coherence prompt for a richer classification.
5. Applies the appropriate CKE operation (MERGE / EXTEND / CONFLICT / EMERGE) via the 
   existing graph mutation layer.
6. Returns a CKEResult describing what happened.
"""

import json
from app.embeddings.similarity import SimilarityService
from app.graph.neo4j_client import neo4j_client
from app.graph.edge_ops import EdgeOperations
from app.graph.mutations import GraphMutations
from app.cke.result import CKEResult, CKEOperation
from app.config.settings import settings
from app.llm.groq_client import groq_client
from app.llm.prompts.coherence_prompts import COHERENCE_PROMPT


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _fetch_all_nodes() -> list[dict]:
    """Return id, text, embedding for every node in Neo4j."""
    query = """
    MATCH (n)
    WHERE n.embedding IS NOT NULL
    RETURN n.id AS id, n.text AS text, n.embedding AS embedding
    """
    return neo4j_client.execute_query(query)


def _llm_classify(existing_text: str, incoming_text: str) -> CKEOperation:
    """
    Ask Groq to classify the relationship between two pieces of knowledge.
    Expected response: one word — MERGE | EXTEND | CONFLICT | EMERGE
    """
    prompt = COHERENCE_PROMPT.format(
        existing=existing_text,
        incoming=incoming_text
    )
    try:
        response = groq_client.generate(prompt, temperature=0.1)
        # Parse the first word that matches a known operation
        response_upper = response.upper()
        for op in ["MERGE", "CONFLICT", "EXTEND", "EMERGE"]:
            if op in response_upper:
                return CKEOperation(op)
    except Exception:
        pass
    # Default — treat as a new isolated concept
    return CKEOperation.NONE


def _apply_operation(
    operation: CKEOperation,
    source_id: str,
    target_id: str,
    score: float,
    llm_explanation: str
) -> CKEResult:
    """Apply the chosen CKE operation and return a CKEResult."""

    if operation == CKEOperation.MERGE:
        # Reinforce the existing node and record the provenance link
        GraphMutations.reinforce(target_id, amount=0.15)
        GraphMutations.increment_version(target_id)
        EdgeOperations.create_relation(source_id, target_id, "SUPPORTS", weight=score)
        return CKEResult(
            operation=CKEOperation.MERGE,
            source_node=source_id,
            target_node=target_id,
            confidence=score,
            explanation=f"Merged: {llm_explanation}"
        )

    elif operation == CKEOperation.EXTEND:
        EdgeOperations.create_relation(source_id, target_id, "EXTENDS", weight=score)
        return CKEResult(
            operation=CKEOperation.EXTEND,
            source_node=source_id,
            target_node=target_id,
            confidence=score,
            explanation=f"Extended: {llm_explanation}"
        )

    elif operation == CKEOperation.CONFLICT:
        EdgeOperations.create_relation(source_id, target_id, "CONTRADICTS", weight=score)
        return CKEResult(
            operation=CKEOperation.CONFLICT,
            source_node=source_id,
            target_node=target_id,
            confidence=score,
            explanation=f"Contradiction flagged: {llm_explanation}"
        )

    elif operation == CKEOperation.EMERGE:
        EdgeOperations.create_relation(source_id, target_id, "EMERGES_FROM", weight=score)
        return CKEResult(
            operation=CKEOperation.EMERGE,
            source_node=source_id,
            target_node=target_id,
            confidence=score,
            explanation=f"Bridge discovered: {llm_explanation}"
        )

    # NONE — standalone new concept, no edge created
    return CKEResult(
        operation=CKEOperation.NONE,
        source_node=source_id,
        target_node=None,
        confidence=1.0,
        explanation="New standalone concept ingested."
    )


# ─── Main Entry ───────────────────────────────────────────────────────────────

class CoherenceAgent:

    @staticmethod
    def process(new_node_id: str, new_text: str, new_embedding: list[float]) -> CKEResult:
        """
        Core coherence evaluation.

        Given a newly created node, compare it against all existing nodes and
        apply the appropriate CKE operation.
        """
        existing_nodes = _fetch_all_nodes()

        # Filter out the node we just created
        candidates = [n for n in existing_nodes if n.get("id") != new_node_id]

        if not candidates:
            return CKEResult(
                operation=CKEOperation.NONE,
                source_node=new_node_id,
                explanation="First node in graph. No coherence evaluation needed."
            )

        # Find the most similar existing node
        best_score = -1.0
        best_node = None

        for node in candidates:
            existing_embedding = node.get("embedding")
            if not existing_embedding:
                continue
            score = SimilarityService.cosine_similarity(new_embedding, existing_embedding)
            if score > best_score:
                best_score = score
                best_node = node

        if best_node is None or best_score < settings.EMERGE_THRESHOLD:
            # No meaningful relationship found
            return CKEResult(
                operation=CKEOperation.NONE,
                source_node=new_node_id,
                explanation=f"No similar node found (best score={best_score:.2f}). Stored as isolated concept."
            )

        # Use LLM to get a nuanced classification + explanation
        llm_prompt = COHERENCE_PROMPT.format(
            existing=best_node.get("text", ""),
            incoming=new_text
        )
        try:
            llm_response = groq_client.generate(llm_prompt, temperature=0.1)
        except Exception as e:
            llm_response = f"LLM unavailable: {e}"

        # Parse the LLM response for an operation keyword
        llm_operation = CKEOperation.NONE
        response_upper = llm_response.upper()
        for op in ["MERGE", "CONFLICT", "EXTEND", "EMERGE"]:
            if op in response_upper:
                llm_operation = CKEOperation(op)
                break

        # Fallback to threshold-based classification if LLM gave no clear answer
        if llm_operation == CKEOperation.NONE:
            if best_score >= settings.MERGE_THRESHOLD:
                llm_operation = CKEOperation.MERGE
            elif best_score >= settings.EXTEND_THRESHOLD:
                llm_operation = CKEOperation.EXTEND
            elif best_score <= settings.CONFLICT_THRESHOLD:
                llm_operation = CKEOperation.CONFLICT
            else:
                llm_operation = CKEOperation.EMERGE

        return _apply_operation(
            operation=llm_operation,
            source_id=new_node_id,
            target_id=best_node["id"],
            score=best_score,
            llm_explanation=llm_response[:300]  # Trim for storage
        )