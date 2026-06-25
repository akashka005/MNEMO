from enum import Enum
from pydantic import BaseModel

class CKEOperation(str, Enum):
    MERGE = "MERGE"
    CONFLICT = "CONFLICT"
    EXTEND = "EXTEND"
    EMERGE = "EMERGE"
    NONE = "NONE"
class CKEResult(BaseModel):
    operation: CKEOperation
    source_node: str | None = None
    target_node: str | None = None
    confidence: float = 0.0
    explanation: str = ""