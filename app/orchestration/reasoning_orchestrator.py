from app.cke.contradiction_detector import (
    ContradictionDetector
)

from app.retrieval.query_retriever import (
    QueryRetriever
)


class ReasoningOrchestrator:

    @staticmethod
    def reason(question: str):

        sources = QueryRetriever.retrieve(
            question
        )

        texts = [
            node["text"]
            for node in sources
            if "text" in node
        ]

        contradictions = (
            ContradictionDetector.detect(
                texts
            )
        )

        return {
            "question": question,
            "sources": sources,
            "contradictions": contradictions
        }