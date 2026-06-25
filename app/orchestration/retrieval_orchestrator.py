from app.agents.query_agent import (
    QueryAgent
)


class RetrievalOrchestrator:

    @staticmethod
    def retrieve(question: str):

        return QueryAgent.answer(
            question
        )