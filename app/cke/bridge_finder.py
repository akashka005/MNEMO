from app.graph.neo4j_client import (
    neo4j_client
)

class BridgeFinder:
    @staticmethod
    def find_bridges():
        query = """
        MATCH (a)-[]->(b)

        WHERE labels(a) <> labels(b)

        RETURN
            labels(a) AS source,
            labels(b) AS target,
            count(*) AS frequency

        ORDER BY frequency DESC
        """
        return (
            neo4j_client.execute_query(
                query
            )
        )