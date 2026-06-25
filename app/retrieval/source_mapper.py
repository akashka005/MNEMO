from app.graph.traversal import GraphTraversal


class SourceMapper:

    @staticmethod
    def map_nodes(node_ids: list[str]):

        sources = []

        for node_id in node_ids:

            node = GraphTraversal.get_node(
                node_id
            )

            if node:
                sources.append(node)

        return sources