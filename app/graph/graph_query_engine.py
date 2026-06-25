from app.graph.neo4j_store import (
    Neo4jStore
)


class GraphQueryEngine:

    @staticmethod
    def search(
        concept
    ):

        query = """
        MATCH (c:Concept {
            name:$concept
        })

        OPTIONAL MATCH
        (c)-[r]->(n)

        RETURN
        c.name AS concept,
        type(r) AS relation,
        n.name AS neighbor
        """

        records = (
            Neo4jStore.query(
                query,
                {
                    "concept": concept
                }
            )
        )

        result = []

        for row in records:

            result.append(
                {
                    "concept": row["concept"],
                    "relation": row["relation"],
                    "neighbor": row["neighbor"]
                }
            )

        return result