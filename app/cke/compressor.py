from app.graph.neo4j_client import (
    neo4j_client
)


class Compressor:

    @staticmethod
    def compress():

        query = """
        MATCH (c:Concept)
        WITH c.text AS text,
             collect(c) AS nodes

        WHERE size(nodes) > 1

        RETURN text,
               size(nodes) AS duplicates
        """

        results = (
            neo4j_client.execute_query(
                query
            )
        )

        return {
            "duplicate_groups":
            len(results),
            "details":
            results
        }