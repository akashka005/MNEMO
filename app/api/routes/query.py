from fastapi import APIRouter
from app.api.schemas.query_schema import QueryRequest, QueryResponse
from app.agents.dialogue_agent import DialogueAgent

router = APIRouter(
    prefix="/query",
    tags=["Query"]
)

@router.post("/", response_model=QueryResponse)
async def query_knowledge(request: QueryRequest):
    result = DialogueAgent.answer(
        question=request.question,
        mode=getattr(request, 'mode', 'factual')
    )
    return QueryResponse(
        question=request.question,
        answer=result["answer"],
        sources=result["sources"]
    )