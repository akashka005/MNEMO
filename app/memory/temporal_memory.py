from collections import defaultdict
from datetime import datetime

class TemporalMemory:
    def __init__(self):

        self.timeline = defaultdict(list)
    def add_version(
        self,
        node_id: str,
        data: dict
    ):
        self.timeline[node_id].append(
            {
                "timestamp": datetime.utcnow(),
                "data": data
            }
        )
    def get_history(
        self,
        node_id: str
    ):
        return self.timeline.get(
            node_id,
            []
        )
temporal_memory = TemporalMemory()