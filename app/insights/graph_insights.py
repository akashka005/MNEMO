from app.graph.traversal import (
    GraphTraversal
)

from app.insights.pattern_detector import (
    PatternDetector
)

from app.insights.contradiction_detector import (
    ContradictionDetector
)


class GraphInsights:

    @staticmethod
    def generate():

        nodes = (
            GraphTraversal
            .get_all_nodes()
        )

        return {
            "patterns":
            PatternDetector.detect(
                nodes
            ),

            "contradictions":
            ContradictionDetector.detect(
                nodes
            ),

            "total_nodes":
            len(nodes)
        }