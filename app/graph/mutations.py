from app.graph.neo4j_client import neo4j_client


class GraphMutations:

    @staticmethod
    def increment_version(
        node_id: str
    ):

        query = """
        MATCH (n {id:$id})

        SET n.version = n.version + 1

        RETURN n
        """

        return neo4j_client.execute_query(
            query,
            {"id": node_id}
        )

    @staticmethod
    def reinforce(
        node_id: str,
        amount: float = 0.1
    ):

        query = """
        MATCH (n {id:$id})

        SET n.confidence =
            n.confidence + $amount

        RETURN n
        """

        return neo4j_client.execute_query(
            query,
            {
                "id": node_id,
                "amount": amount
            }
        )