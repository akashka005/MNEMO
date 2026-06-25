from app.graph.mutations import GraphMutations

class ReinforceOperation:
    @staticmethod
    def execute(
        node_id: str,
        amount: float = 0.1
    ):
        return GraphMutations.reinforce(
            node_id,
            amount
        )