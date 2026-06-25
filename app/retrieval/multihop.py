from app.graph.traversal import GraphTraversal

class MultiHopRetriever:
    @staticmethod
    def expand(
        node_id: str,
        hops: int = 2
    ):
        visited = set()
        frontier = [node_id]
        results = []
        for _ in range(hops):
            next_frontier = []
            for current in frontier:
                if current in visited:
                    continue
                visited.add(current)
                neighbors = (
                    GraphTraversal.get_neighbors(
                        current
                    )
                )
                for n in neighbors:
                    results.append(n)
                    next_frontier.append(
                        n["id"]
                    )
            frontier = next_frontier
        return results