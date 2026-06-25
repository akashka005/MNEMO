from app.graph.graph_writer import (
    GraphWriter
)

from app.graph.hypothesis_writer import (
    HypothesisWriter
)

from app.graph.lifecycle_writer import (
    LifecycleWriter
)

from app.graph.graph_query_engine import (
    GraphQueryEngine
)

from app.graph.graph_reasoner import (
    GraphReasoner
)


class PhaseHPipeline:

    @staticmethod
    def run():

        GraphWriter.create_concept(
            "Transformer"
        )

        GraphWriter.create_concept(
            "Attention"
        )

        HypothesisWriter.write(
            "Transformer",
            "Long Context",
            0.7
        )

        LifecycleWriter.update(
            "Transformer"
        )

        graph = (
            GraphQueryEngine.search(
                "Transformer"
            )
        )

        inferred = (
            GraphReasoner.infer()
        )

        return {
            "graph": graph,
            "inferred": inferred
        }