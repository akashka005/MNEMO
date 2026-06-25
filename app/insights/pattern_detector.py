from collections import Counter


class PatternDetector:

    @staticmethod
    def detect(nodes):

        words = []

        for node in nodes:
            text = (
                node.get("text", "")
                .lower()
                .split()
            )

            words.extend(text)

        counts = Counter(words)

        return [
            {
                "term": term,
                "count": count
            }
            for term, count
            in counts.items()
            if count > 1
        ]