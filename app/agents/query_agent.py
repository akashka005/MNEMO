from app.retrieval.query_retriever import (
    QueryRetriever
)
from app.retrieval.context_builder import (
    ContextBuilder
)
from app.llm.groq_client import (
    groq_client
)
from app.llm.prompts.dialogue_prompts import (
    RAG_PROMPT
)

class QueryAgent:
    @staticmethod
    def answer(
        question: str
    ):
        nodes = (
            QueryRetriever.retrieve(
                question
            )
        )
        context = (
            ContextBuilder.build(
                question,
                nodes
            )
        )
        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )
        answer = (
            groq_client.generate(
                prompt
            )
        )
        return {
            "question": question,
            "answer": answer,
            "sources": [
                node["id"]
                for node in nodes
            ]
        }