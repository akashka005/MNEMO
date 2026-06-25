from app.orchestration.workflow import (
    Workflow
)

class ReasoningLoop:
    @staticmethod
    def run(query: str):
        result = Workflow.execute(
            query
        )
        return result