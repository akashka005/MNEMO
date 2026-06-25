class MemoryPruner:
    @staticmethod
    def prune(
        nodes,
        min_confidence=0.3
    ):
        kept = []
        for node in nodes:
            confidence = (
                node.get(
                    "confidence",
                    1.0
                )
            )
            if confidence >= min_confidence:
                kept.append(node)
        return kept