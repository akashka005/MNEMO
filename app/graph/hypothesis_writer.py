from app.graph.neo4j_store import (
    Neo4jStore
)


class HypothesisWriter:

    @staticmethod
    def write(
        source,
        target,
        confidence=0.7
    ):

        query = """
        MERGE (a:Concept {
            name:$source
        })

        MERGE (b:Concept {
            name:$target
        })

        MERGE (a)-[
            r:HYPOTHESIS
        ]->(b)

        SET r.confidence =
            $confidence
        """

        Neo4jStore.execute(
            query,
            {
                "source": source,
                "target": target,
                "confidence": confidence
            }
        )

        return True