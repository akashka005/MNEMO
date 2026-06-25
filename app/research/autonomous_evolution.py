from app.cke.concept_merger import (
    ConceptMerger
)

from app.cke.contradiction_resolver import (
    ContradictionResolver
)

from app.cke.memory_pruner import (
    MemoryPruner
)

from app.research.hypothesis_generator import (
    HypothesisGenerator
)


class AutonomousEvolution:

    @staticmethod
    def evolve(
        concepts,
        texts,
        edges,
        nodes
    ):

        merged = (
            ConceptMerger.merge(
                concepts
            )
        )

        contradictions = (
            ContradictionResolver.resolve(
                texts
            )
        )

        hypotheses = (
            HypothesisGenerator.generate(
                edges
            )
        )

        pruned_nodes = (
            MemoryPruner.prune(
                nodes
            )
        )

        return {
            "merged": merged,
            "contradictions": contradictions,
            "hypotheses": hypotheses,
            "nodes": pruned_nodes
        }