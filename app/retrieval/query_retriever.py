from app.embeddings.embedder import embedder
from app.graph.traversal import GraphTraversal


class QueryRetriever:

    @staticmethod
    def retrieve(
        question: str,
        top_k: int = 5
    ):

        embedding = embedder.embed_text(
            question
        )

        return GraphTraversal.get_similar_nodes(
            embedding=embedding,
            top_k=top_k
        )