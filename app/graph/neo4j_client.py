from neo4j import GraphDatabase

from app.config.settings import settings


class Neo4jClient:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USER,
                settings.NEO4J_PASSWORD
            )
        )

    def execute_query(
        self,
        query: str,
        parameters: dict = None
    ):

        with self.driver.session() as session:

            result = session.run(
                query,
                parameters or {}
            )

            return list(result)

    def close(self):

        self.driver.close()


neo4j_client = Neo4jClient()