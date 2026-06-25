class CoherenceMetrics:

    @staticmethod
    def graph_density(
        total_nodes: int,
        total_edges: int
    ):

        if total_nodes <= 1:
            return 0

        max_edges = (
            total_nodes *
            (total_nodes - 1)
        )

        return total_edges / max_edges

    @staticmethod
    def contradiction_ratio(
        contradictions: int,
        total_nodes: int
    ):

        if total_nodes == 0:
            return 0

        return contradictions / total_nodes

    @staticmethod
    def merge_compression(
        merged_nodes: int,
        original_nodes: int
    ):

        if original_nodes == 0:
            return 0

        return merged_nodes / original_nodes