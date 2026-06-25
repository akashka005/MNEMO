class ConfidenceMemory:
    def __init__(self):
        self.scores = {}
    def set_score(
        self,
        node_id: str,
        score: float
    ):
        self.scores[node_id] = score
    def get_score(
        self,
        node_id: str
    ):
        return self.scores.get(
            node_id,
            1.0
        )
    def reinforce(
        self,
        node_id: str,
        amount: float = 0.05
    ):
        current = self.get_score(node_id)
        self.scores[node_id] = min(
            1.0,
            current + amount
        )
    def decay(
        self,
        node_id: str,
        amount: float = 0.05
    ):
        current = self.get_score(node_id)
        self.scores[node_id] = max(
            0.0,
            current - amount
        )
confidence_memory = ConfidenceMemory()