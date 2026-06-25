from collections import Counter

class BridgeDiscovery:
    @staticmethod
    def evaluate(
        sources: list
    ) -> float:
        if not sources:
            return 0.0
        labels = []
        for source in sources:
            if isinstance(source, dict):
                labels.extend(
                    source.keys()
                )
        unique_labels = len(
            set(labels)
        )
        total_labels = len(labels)
        if total_labels == 0:
            return 0.0
        return round(
            unique_labels /
            total_labels,
            2
        )