from app.evaluation.baseline_rag import (
    BaselineRAG
)

from app.evaluation.metrics.coherence_score import (
    CoherenceScore
)

from app.evaluation.metrics.contradiction_accuracy import (
    ContradictionAccuracy
)

from app.evaluation.report_generator import (
    ReportGenerator
)


def main():

    result = BaselineRAG.answer(
        "What do transformers use?"
    )

    coherence = (
        CoherenceScore.evaluate(
            result["answer"]
        )
    )

    contradiction = (
        ContradictionAccuracy.evaluate(
            "app/evaluation/datasets/contradiction_pairs.json"
        )
    )

    report = (
        ReportGenerator.generate(
            coherence,
            contradiction
        )
    )

    print("\n==========")
    print("MENMO EVAL")
    print("==========")

    for k, v in report.items():
        print(
            f"{k}: {v}"
        )


if __name__ == "__main__":
    main()