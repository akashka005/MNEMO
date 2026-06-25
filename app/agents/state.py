from typing import Any
from typing import Dict
from typing import List
from pydantic import BaseModel, Field

class AgentState(BaseModel):
    text: str | None = None
    node_id: str | None = None
    embedding: List[float] | None = None
    related_nodes: List[Dict[str, Any]] = Field(
        default_factory=list
    )
    cke_result: Dict[str, Any] | None = None
    answer: str | None = None
    last_operation: str | None = None
    confidence: float | None = None