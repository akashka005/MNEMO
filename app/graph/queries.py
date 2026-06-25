from app.graph.neo4j_client import neo4j_client


class GraphQueries:

    @staticmethod
    def all_nodes():

        query = """
        MATCH (n)

        RETURN n
        """

        return neo4j_client.execute_query(
            query
        )

    @staticmethod
    def all_edges():

        query = """
        MATCH ()-[r]->()

        RETURN r
        """

        return neo4j_client.execute_query(
            query
        )

    @staticmethod
    def node_count():

        query = """
        MATCH (n)

        RETURN count(n) AS count
        """

        return neo4j_client.execute_query(
            query
        )

    @staticmethod
    def edge_count():

        query = """
        MATCH ()-[r]->()

        RETURN count(r) AS count
        """

        return neo4j_client.execute_query(
            query
        )