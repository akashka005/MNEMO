class HallucinationRate:

    @staticmethod
    def evaluate(
        answer: str,
        context: str
    ):

        answer_words = set(
            answer.lower().split()
        )

        context_words = set(
            context.lower().split()
        )

        if not answer_words:
            return 1.0

        supported = len(
            answer_words &
            context_words
        )

        rate = 1 - (
            supported /
            len(answer_words)
        )

        return round(
            rate,
            2
        )