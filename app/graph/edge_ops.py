from app.graph.neo4j_client import neo4j_client


class EdgeOperations:

    @staticmethod
    def create_relation(
        source_id: str,
        target_id: str,
        relation: str,
        weight: float = 1.0
    ):

        query = f"""
        MATCH (a {{id:$source}})
        MATCH (b {{id:$target}})

        MERGE (a)-[r:{relation}]->(b)

        SET r.weight = $weight

        RETURN r
        """

        return neo4j_client.execute_query(
            query,
            {
                "source": source_id,
                "target": target_id,
                "weight": weight
            }
        )

    @staticmethod
    def get_relations(
        node_id: str
    ):

        query = """
        MATCH (a {id:$id})-[r]->(b)

        RETURN r,b
        """

        return neo4j_client.execute_query(
            query,
            {"id": node_id}
        )