from app.discovery.hypothesis_engine import (
    HypothesisEngine
)
from app.discovery.experiment_generator import (
    ExperimentGenerator
)
from app.discovery.question_generator import (
    QuestionGenerator
)

class DiscoveryPipeline:
    @staticmethod
    def run(
        graph
    ):
        hypotheses = (
            HypothesisEngine.generate(
                graph
            )
        )
        experiments = (
            ExperimentGenerator.generate(
                hypotheses
            )
        )
        questions = (
            QuestionGenerator.generate(
                graph
            )
        )
        return {
            "hypotheses":
            hypotheses,
            "experiments":
            experiments,
            "questions":
            questions
        }