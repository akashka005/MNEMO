class QuestionGenerator:
    @staticmethod
    def generate(
        graph
    ):
        return [
            f"Why does {edge['source']} affect {edge['target']}?"
            for edge in graph
        ]