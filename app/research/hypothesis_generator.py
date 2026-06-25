class HypothesisGenerator:

    @staticmethod
    def generate(edges):

        normalized = []

        for edge in edges:

            if isinstance(edge, dict):

                normalized.append(
                    (
                        edge.get("source"),
                        edge.get("target")
                    )
                )

            elif (
                isinstance(edge, (list, tuple))
                and len(edge) == 2
            ):

                normalized.append(edge)

        hypotheses = []

        for src1, dst1 in normalized:

            for src2, dst2 in normalized:

                if dst1 == src2:

                    hypothesis = {
                        "source": src1,
                        "target": dst2,
                        "confidence": 0.7
                    }

                    if (
                        src1 != dst2
                        and hypothesis not in hypotheses
                    ):
                        hypotheses.append(
                            hypothesis
                        )

        return hypotheses