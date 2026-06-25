class CompressionRatio:

    @staticmethod
    def evaluate(
        original_text: str,
        stored_text: str
    ) -> float:
        original_size = len(
            original_text.split()
        )
        stored_size = len(
            stored_text.split()
        )
        if original_size == 0:
            return 0.0
        return round(
            stored_size /
            original_size,
            2
        )