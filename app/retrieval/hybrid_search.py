from app.embeddings.embedder import embedder
from app.retrieval.faiss_store import (
    faiss_store
)
from app.graph.traversal import (
    GraphTraversal
)
from app.retrieval.reranker import (
    ReRanker
)
from app.retrieval.multihop import (
    MultiHopRetriever
)

class HybridSearch:
    @staticmethod
    def search(
        question: str,
        top_k: int = 5
    ):
        query_embedding = (
            embedder.embed_text(
                question
            )
        )
        vector_hits = (
            faiss_store.search(
                query_embedding,
                top_k
            )
        )
        enriched = []
        for hit in vector_hits:
            node = (
                GraphTraversal.get_node(
                    hit["node_id"]
                )
            )
            if not node:
                continue
            node["score"] = (
                hit["score"]
            )
            enriched.append(
                node
            )
        ranked = (
            ReRanker.rerank(
                enriched
            )
        )
        return ranked