class GraphUtils:

    @staticmethod
    def build_edge(
        source: str,
        target: str,
        relation: str,
        weight: float = 1.0
    ):

        return {
            "source": source,
            "target": target,
            "relation": relation,
            "weight": weight
        }

    @staticmethod
    def build_node(
        node_id: str,
        label: str,
        confidence: float = 1.0
    ):

        return {
            "id": node_id,
            "label": label,
            "confidence": confidence
        }