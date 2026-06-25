from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Question to query the user."
    )
    mode: str = Field(
        default="factual",
        description="Mode of the agent (factual or socratic)"
    )
class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[str] = []