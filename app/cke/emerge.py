from app.cke.base import BaseCKEOperation
from app.cke.result import (
    CKEResult,
    CKEOperation
)
from app.graph.edge_ops import EdgeOperations

class EmergeOperation(
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
            "EMERGES_FROM"
        )
        return CKEResult(
            operation=CKEOperation.EMERGE,
            source_node=source_node_id,
            target_node=target_node_id,
            confidence=1.0,
            explanation="Emergent bridge discovered."
        )