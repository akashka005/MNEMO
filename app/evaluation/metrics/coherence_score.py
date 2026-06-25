class CoherenceScore:

    @staticmethod
    def evaluate(
        answer: str
    ) -> float:
        if not answer:
            return 0.0
        sentences = [
            s.strip()
            for s in answer.split(".")
            if s.strip()
        ]
        if len(sentences) == 0:
            return 0.0
        return min(
            1.0,
            len(sentences) / 5
        )