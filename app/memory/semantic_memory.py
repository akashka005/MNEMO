from app.graph.node_ops import NodeOperations
from app.graph.traversal import GraphTraversal

class SemanticMemory:
    @staticmethod
    def store(
        text,
        embedding,
        node_type="concept"
    ):
        return NodeOperations.create_node(
            text=text,
            embedding=embedding,
            node_type=node_type
        )
    @staticmethod
    def retrieve(
        embedding,
        top_k=5
    ):
        return GraphTraversal.get_similar_nodes(
            embedding,
            top_k=top_k
        )