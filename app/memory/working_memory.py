from collections import deque
from typing import Dict, List

class WorkingMemory:

    def __init__(self, max_size: int = 20):
        self.max_size = max_size
        self.memory = deque(maxlen=max_size)
    def add(self, item: Dict):
        self.memory.append(item)
    def get_all(self) -> List[Dict]:
        return list(self.memory)
    def latest(self):
        if not self.memory:
            return None
        return self.memory[-1]
    def clear(self):
        self.memory.clear()
working_memory = WorkingMemory()