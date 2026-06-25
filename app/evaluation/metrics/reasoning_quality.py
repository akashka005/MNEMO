class ReasoningQuality:

    REASONING_TERMS = [
        "because",
        "therefore",
        "thus",
        "hence",
        "since",
        "as a result",
        "consequently",
        "which means"
    ]

    @staticmethod
    def evaluate(
        answer: str
    ) -> float:

        answer = answer.lower()

        count = 0

        for term in (
            ReasoningQuality
            .REASONING_TERMS
        ):

            if term in answer:
                count += 1

        score = min(
            count /
            len(
                ReasoningQuality
                .REASONING_TERMS
            ),
            1.0
        )

        return round(
            score,
            2
        )