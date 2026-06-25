from app.graph.traversal import GraphTraversal

class RetrievalAgent:
    @staticmethod
    def retrieve(
        query_embedding,
        top_k: int = 5
    ):
        return GraphTraversal.get_similar_nodes(
            query_embedding,
            top_k=top_k
        )