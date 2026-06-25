from app.research.autonomous_evolution import (
    AutonomousEvolution
)

from app.research.memory_health_monitor import (
    MemoryHealthMonitor
)


class GraphEvolutionPipeline:

    @staticmethod
    def run():

        concepts = [
            "LLM",
            "llm",
            "Transformer"
        ]

        texts = [
            "Transformers use attention",
            "Transformers do not use attention"
        ]

        edges = [
            ("Transformer", "Attention"),
            ("Attention", "Long Context")
        ]

        nodes = [
            {
                "text": "Transformer",
                "confidence": 0.95
            },
            {
                "text": "Old Concept",
                "confidence": 0.1
            }
        ]

        evolution = (
            AutonomousEvolution.evolve(
                concepts,
                texts,
                edges,
                nodes
            )
        )

        health = (
            MemoryHealthMonitor.evaluate(
                nodes=evolution["nodes"],
                edges=edges,
                contradictions=evolution[
                    "contradictions"
                ],
                hypotheses=evolution[
                    "hypotheses"
                ]
            )
        )

        return {
            "evolution": evolution,
            "health": health
        }