from typing import List, Dict, Optional

from app.graph.neo4j_client import neo4j_client
from app.embeddings.similarity import SimilarityService


class GraphTraversal:

    @staticmethod
    def get_similar_nodes(
        embedding: List[float],
        current_node_id: Optional[str] = None,
        top_k: int = 5,
        min_similarity: float = 0.30
    ) -> List[Dict]:

        query = """
        MATCH (n)

        RETURN
            n.id AS id,
            n.text AS text,
            n.embedding AS embedding,
            n.confidence AS confidence,
            labels(n) AS labels
        """

        records = neo4j_client.execute_query(query)

        scored_nodes = []

        for node in records:

            if (
                current_node_id is not None and
                node["id"] == current_node_id
            ):
                continue

            node_embedding = node.get("embedding")

            if not node_embedding:
                continue

            try:

                similarity = (
                    SimilarityService.cosine_similarity(
                        embedding,
                        node_embedding
                    )
                )

            except Exception:
                continue

            if similarity < min_similarity:
                continue

            scored_nodes.append(
                {
                    "id": node["id"],
                    "text": node.get("text"),
                    "embedding": node_embedding,
                    "confidence": node.get(
                        "confidence",
                        1.0
                    ),
                    "labels": node.get(
                        "labels",
                        []
                    ),
                    "score": similarity
                }
            )

        scored_nodes.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return scored_nodes[:top_k]

    @staticmethod
    def get_neighbors(
        node_id: str
    ) -> List[Dict]:

        query = """
        MATCH (a)-[r]-(b)

        WHERE a.id = $node_id

        RETURN
            b.id AS id,
            b.text AS text,
            type(r) AS relation,
            b.confidence AS confidence
        """

        return neo4j_client.execute_query(
            query,
            {"node_id": node_id}
        )

    @staticmethod
    def get_node(
        node_id: str
    ) -> Optional[Dict]:

        query = """
        MATCH (n)

        WHERE n.id = $node_id

        RETURN
            n.id AS id,
            n.text AS text,
            n.embedding AS embedding,
            n.confidence AS confidence,
            labels(n) AS labels

        LIMIT 1
        """

        result = neo4j_client.execute_query(
            query,
            {"node_id": node_id}
        )

        if result:
            return result[0]

        return None

    @staticmethod
    def find_path(
        source_id: str,
        target_id: str,
        max_hops: int = 3
    ):

        query = f"""
        MATCH p=shortestPath(
            (a {{id:$source}})
            -[*..{max_hops}]-
            (b {{id:$target}})
        )

        RETURN p
        """

        return neo4j_client.execute_query(
            query,
            {
                "source": source_id,
                "target": target_id
            }
        )

    @staticmethod
    def get_subgraph(
        node_id: str,
        depth: int = 2
    ):

        query = f"""
        MATCH p=(n {{id:$node_id}})
        -[*..{depth}]-
        (m)

        RETURN p
        """

        return neo4j_client.execute_query(
            query,
            {"node_id": node_id}
        )

    @staticmethod
    def node_exists(
        node_id: str
    ) -> bool:

        query = """
        MATCH (n)

        WHERE n.id = $node_id

        RETURN count(n) AS count
        """

        result = neo4j_client.execute_query(
            query,
            {"node_id": node_id}
        )

        return result[0]["count"] > 0

    @staticmethod
    def total_nodes() -> int:

        query = """
        MATCH (n)

        RETURN count(n) AS total
        """

        result = neo4j_client.execute_query(query)

        return result[0]["total"]

    @staticmethod
    def total_edges() -> int:

        query = """
        MATCH ()-[r]->()

        RETURN count(r) AS total
        """

        result = neo4j_client.execute_query(query)

        return result[0]["total"]