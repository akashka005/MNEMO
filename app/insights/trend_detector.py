from collections import Counter

from app.graph.neo4j_client import (
    neo4j_client
)


class TrendDetector:

    @staticmethod
    def detect(
        texts=None
    ):
        if texts:

            words = []

            for text in texts:

                words.extend(
                    text.lower().split()
                )

            trends = (
                Counter(words)
                .most_common(10)
            )

            return [
                {
                    "concept": word,
                    "frequency": freq
                }
                for word, freq in trends
            ]

        query = """
        MATCH (n)
        RETURN n.text AS text
        """

        results = (
            neo4j_client.execute_query(
                query
            )
        )

        words = []

        for row in results:

            if row.get("text"):

                words.extend(
                    row["text"]
                    .lower()
                    .split()
                )

        trends = (
            Counter(words)
            .most_common(10)
        )

        return [
            {
                "concept": word,
                "frequency": freq
            }
            for word, freq in trends
        ]