from app.orchestration.routing import Router
from app.orchestration.graph_pipeline import (
    GraphPipeline
)

class Workflow:
    @staticmethod
    def execute(query: str):
        route = Router.route(query)
        if route.value == "INGEST":
            return GraphPipeline.process(
                query
            )
        return {
            "route": route.value,
            "query": query
        }