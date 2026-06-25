from app.cke.base import BaseCKEOperation
from app.cke.result import CKEResult
from app.cke.result import CKEOperation
from app.graph.mutations import GraphMutations

class MergeOperation(
    BaseCKEOperation
):
    def execute(
        self,
        source_node_id: str,
        target_node_id: str
    ):
        GraphMutations.increment_version(
            target_node_id
        )
        GraphMutations.reinforce(
            target_node_id,
            amount=0.2
        )
        return CKEResult(
            operation=CKEOperation.MERGE,
            source_node=source_node_id,
            target_node=target_node_id,
            confidence=1.0,
            explanation="Knowledge merged."
        )