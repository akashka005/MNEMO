class HypothesisEngine:
    @staticmethod
    def generate(
        graph
    ):
        hypotheses = []
        for edge in graph:
            hypotheses.append(
                {
                    "hypothesis":
                    f"{edge['source']} may improve {edge['target']}"
                }
            )
        return hypotheses