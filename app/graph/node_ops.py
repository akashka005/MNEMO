import uuid

from app.graph.neo4j_client import neo4j_client


class NodeOperations:

    @staticmethod
    def create_node(
        text: str,
        node_type: str,
        embedding: list[float],
        confidence: float = 1.0
    ):

        node_id = str(uuid.uuid4())

        query = """
        CREATE (n:%s {
            id:$id,
            text:$text,
            embedding:$embedding,
            confidence:$confidence,
            version:1
        })
        RETURN n
        """ % node_type

        neo4j_client.execute_query(
            query,
            {
                "id": node_id,
                "text": text,
                "embedding": embedding,
                "confidence": confidence
            }
        )

        return node_id

    @staticmethod
    def get_node(
        node_id: str
    ):

        query = """
        MATCH (n {id:$id})
        RETURN n
        """

        result = neo4j_client.execute_query(
            query,
            {"id": node_id}
        )

        return result

    @staticmethod
    def update_confidence(
        node_id: str,
        confidence: float
    ):

        query = """
        MATCH (n {id:$id})

        SET n.confidence = $confidence

        RETURN n
        """

        return neo4j_client.execute_query(
            query,
            {
                "id": node_id,
                "confidence": confidence
            }
        )

    @staticmethod
    def delete_node(
        node_id: str
    ):

        query = """
        MATCH (n {id:$id})

        DETACH DELETE n
        """

        neo4j_client.execute_query(
            query,
            {"id": node_id}
        )