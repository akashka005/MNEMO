class MemoryHealthMonitor:

    @staticmethod
    def evaluate(
        nodes,
        edges,
        contradictions,
        hypotheses
    ):

        return {
            "nodes": len(nodes),
            "edges": len(edges),
            "contradictions": len(
                contradictions
            ),
            "hypotheses": len(
                hypotheses
            ),
            "health_score":
                round(
                    (
                        len(nodes)
                        + len(edges)
                    )
                    /
                    (
                        1
                        + len(
                            contradictions
                        )
                    ),
                    2
                )
        }