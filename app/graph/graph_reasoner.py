from app.graph.neo4j_store import (
    Neo4jStore
)


class GraphReasoner:

    @staticmethod
    def infer():

        query = """
        MATCH
        (a)-[:RELATED_TO]->(b),
        (b)-[:RELATED_TO]->(c)

        WHERE a <> c

        MERGE
        (a)-[:INFERRED]->(c)

        RETURN
        a.name AS source,
        c.name AS target
        """

        records = (
            Neo4jStore.query(
                query
            )
        )

        result = []

        for row in records:

            result.append(
                {
                    "source": row["source"],
                    "target": row["target"]
                }
            )

        return result