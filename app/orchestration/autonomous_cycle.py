from app.insights.trend_analysis import (
    TrendAnalysis
)

from app.insights.research_gap_detector import (
    ResearchGapDetector
)

from app.insights.novelty_detector import (
    NoveltyDetector
)


class AutonomousCycle:

    @staticmethod
    def run():

        return {
            "trends":
                TrendAnalysis.detect(),

            "gaps":
                ResearchGapDetector.detect(),

            "novelty":
                NoveltyDetector.detect()
        }