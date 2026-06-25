class ExperimentGenerator:
    @staticmethod
    def generate(
        hypotheses
    ):
        experiments = []
        for h in hypotheses:
            experiments.append(
                {
                    "experiment":
                    f"Test: {h['hypothesis']}"
                }
            )
        return experiments