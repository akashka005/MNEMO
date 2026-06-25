import uuid
from app.embeddings.embedder import embedder
from app.graph.node_ops import NodeOperations
from app.agents.coherence_agent import CoherenceAgent

class IngestionAgent:
    @staticmethod
    def ingest(text: str):
        # 1. Embed the incoming text
        embedding = embedder.embed_text(text)

        # 2. Create a node in Neo4j
        node_id = NodeOperations.create_node(
            text=text,
            embedding=embedding,
            node_type="Concept"
        )

        # 3. Run the Coherence Agent — compare against existing nodes
        cke_result = CoherenceAgent.process(
            new_node_id=node_id,
            new_text=text,
            new_embedding=embedding
        )

        return {
            "node_id": node_id,
            "text": text[:200],  # Truncate for response
            "cke_operation": cke_result.operation.value,
            "cke_target": cke_result.target_node,
            "cke_explanation": cke_result.explanation
        }