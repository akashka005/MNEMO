from app.graph.neo4j_store import (
    Neo4jStore
)


class GraphWriter:

    @staticmethod
    def create_concept(
        concept
    ):

        query = """
        MERGE (
            c:Concept {
                name:$concept
            }
        )
        """

        Neo4jStore.execute(
            query,
            {
                "concept": concept
            }
        )

        return True