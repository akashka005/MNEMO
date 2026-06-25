class ReportGenerator:

    @staticmethod
    def generate(
        coherence,
        contradiction_accuracy
    ):

        overall = (
            coherence +
            contradiction_accuracy
        ) / 2

        return {
            "coherence": round(
                coherence,
                3
            ),

            "contradiction_accuracy":
            round(
                contradiction_accuracy,
                3
            ),

            "overall_score":
            round(
                overall,
                3
            )
        }