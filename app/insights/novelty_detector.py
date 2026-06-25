from app.graph.neo4j_client import (
    neo4j_client
)


class NoveltyDetector:

    @staticmethod
    def detect(graph=None):
        if graph is not None:

            novelty = []

            for edge in graph:

                source = edge.get(
                    "source"
                )

                target = edge.get(
                    "target"
                )

                if source and target:

                    novelty.append(
                        (
                            source,
                            target
                        )
                    )

            return novelty
        query = """
        MATCH (a)-[r]->(b)

        RETURN
            a.text AS source,
            type(r) AS relation,
            b.text AS target
        """

        results = (
            neo4j_client.execute_query(
                query
            )
        )

        novelty = []

        for row in results:

            novelty.append(
                (
                    row["source"],
                    row["target"]
                )
            )

        return novelty