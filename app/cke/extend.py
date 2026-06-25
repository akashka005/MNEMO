from app.cke.base import BaseCKEOperation
from app.cke.result import (
    CKEResult,
    CKEOperation
)
from app.graph.edge_ops import EdgeOperations

class ExtendOperation(
    BaseCKEOperation
):
    def execute(
        self,
        source_node_id,
        target_node_id
    ):
        EdgeOperations.create_relation(
            source_node_id,
            target_node_id,
            "EXTENDS"
        )
        return CKEResult(
            operation=CKEOperation.EXTEND,
            source_node=source_node_id,
            target_node=target_node_id,
            confidence=1.0,
            explanation="Knowledge extension."
        )