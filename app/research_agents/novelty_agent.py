from app.insights.novelty_detector import (
    NoveltyDetector
)


class NoveltyAgent:

    @staticmethod
    def score(graph):

        novelty = (
            NoveltyDetector.detect(
                graph
            )
        )

        return {
            "novelty_count": len(
                novelty
            ),
            "novelty": novelty
        }