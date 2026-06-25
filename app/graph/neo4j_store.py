from app.graph.neo4j_client import (
    neo4j_client
)


class Neo4jStore:

    @staticmethod
    def query(
        query: str,
        params: dict = None
    ):

        return (
            neo4j_client.execute_query(
                query,
                params
            )
        )

    @staticmethod
    def execute(
        query: str,
        params: dict = None
    ):

        return (
            neo4j_client.execute_query(
                query,
                params
            )
        )