from app.graph.neo4j_client import (
    neo4j_client
)

class EvolutionTracker:
    @staticmethod
    def stats():
        query = """
        MATCH (n)
        RETURN count(n) AS total_nodes
        """
        result = (
            neo4j_client.execute_query(
                query
            )
        )
        if not result:
            return {
                "total_nodes": 0
            }
        return {
            "total_nodes":
            result[0]["total_nodes"]
        }