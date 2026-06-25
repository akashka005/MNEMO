from app.cke.base import BaseCKEOperation
from app.cke.result import (
    CKEResult,
    CKEOperation
)
from app.graph.edge_ops import EdgeOperations

class ConflictOperation(
    BaseCKEOperation
):
    def execute(
        self,
        source_node_id: str,
        target_node_id: str
    ):
        EdgeOperations.create_relation(
            source_node_id,
            target_node_id,
            "CONTRADICTS"
        )
        return CKEResult(
            operation=CKEOperation.CONFLICT,
            source_node=source_node_id,
            target_node=target_node_id,
            confidence=1.0,
            explanation="Contradiction detected."
        )