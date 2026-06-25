from datetime import datetime

from app.graph.neo4j_store import (
    Neo4jStore
)


class LifecycleWriter:

    @staticmethod
    def update(
        concept,
        confidence=1.0
    ):

        now = str(
            datetime.utcnow()
        )

        query = """
        MERGE (c:Concept {
            name:$concept
        })

        ON CREATE SET
            c.birth_date=$birth_date,
            c.mentions=1

        ON MATCH SET
            c.mentions=
            coalesce(
                c.mentions,
                0
            ) + 1

        SET
            c.last_seen=$last_seen,
            c.confidence=$confidence
        """

        Neo4jStore.execute(
            query,
            {
                "concept": concept,
                "birth_date": now,
                "last_seen": now,
                "confidence": confidence
            }
        )

        return True