from fastapi import APIRouter
from app.research_agents.research_orchestrator import (
    ResearchOrchestrator
)

router = APIRouter()

@router.post(
    "/research/analyze"
)
def analyze(payload: dict):
    texts = payload.get(
        "texts",
        []
    )
    nodes = payload.get(
        "nodes",
        []
    )
    graph = payload.get(
        "graph",
        []
    )
    return (
        ResearchOrchestrator.run(
            texts,
            nodes,
            graph
        )
    )