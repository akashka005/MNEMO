from app.graph.neo4j_client import (
    neo4j_client
)

class ResearchGapDetector:

    @staticmethod
    def detect(texts=None):

        query = """
        MATCH (n)
        WHERE NOT (n)--()
        RETURN n.text AS concept
        """

        results = (
            neo4j_client.execute_query(
                query
            )
        )

        return [
            row["concept"]
            for row in results
            if row.get("concept")
        ]
ResearchGapFinder = ResearchGapDetector