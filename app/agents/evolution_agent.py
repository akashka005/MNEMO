from app.graph.traversal import (
    GraphTraversal
)

class EvolutionAgent:

    @staticmethod
    def get_node_history(
        node_id: str
    ):
        node = (
            GraphTraversal
            .get_node(node_id)
        )
        if not node:
            return None
        return {
            "node_id": node_id,
            "text": node.get("text"),
            "confidence":
            node.get(
                "confidence"
            ),
            "version":
            node.get(
                "version",
                1
            )
        }