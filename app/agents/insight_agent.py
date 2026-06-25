from app.graph.neo4j_client import (
    neo4j_client
)

class InsightAgent:

    @staticmethod
    def get_insights():
        query = """
        MATCH (a)-[r]->(b)

        RETURN
            type(r) AS relation,
            count(r) AS count
        """
        return neo4j_client.execute_query(
            query
        )

    @staticmethod
    def analyze():
        return InsightAgent.get_insights()