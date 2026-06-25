from app.retrieval.query_retriever import QueryRetriever
from app.llm.groq_client import groq_client


class BaselineRAG:

    @staticmethod
    def answer(
        question: str
    ):

        sources = QueryRetriever.retrieve(
            question,
            top_k=3
        )

        context = "\n".join(
            source["text"]
            for source in sources
            if "text" in source
        )

        prompt = f"""
Answer using only the context.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = groq_client.generate(
            prompt
        )

        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }