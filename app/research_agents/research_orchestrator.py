from app.research_agents.literature_agent import (
    LiteratureAgent
)

from app.research_agents.hypothesis_agent import (
    HypothesisAgent
)

from app.research_agents.contradiction_agent import (
    ContradictionAgent
)

from app.research_agents.novelty_detector import (
    NoveltyDetector
)


class ResearchOrchestrator:

    @staticmethod
    def run(
        texts,
        nodes,
        graph
    ):

        literature = (
            LiteratureAgent.analyze(
                texts
            )
        )

        hypotheses = (
            HypothesisAgent.generate(
                nodes
            )
        )

        contradictions = (
            ContradictionAgent.analyze(
                texts
            )
        )

        novelty = (
            NoveltyDetector.detect(
                texts, nodes
            )
        )

        return {
            "literature": literature,
            "hypotheses": hypotheses,
            "contradictions": contradictions,
            "novelty": novelty
        }