from app.graph.neo4j_client import (
    neo4j_client
)

class DecayOperation:
    @staticmethod
    def execute(
        node_id: str,
        amount: float = 0.05
    ):
        query = """
        MATCH (n {id:$id})

        SET n.confidence =
            n.confidence - $amount

        RETURN n
        """
        return neo4j_client.execute_query(
            query,
            {
                "id": node_id,
                "amount": amount
            }
        )