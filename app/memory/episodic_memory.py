from datetime import datetime

class EpisodicMemory:
    def __init__(self):
        self.events = []
    def add_event(
        self,
        event_type: str,
        payload: dict
    ):
        self.events.append(
            {
                "timestamp": datetime.utcnow(),
                "event_type": event_type,
                "payload": payload
            }
        )
    def recent(
        self,
        limit=20
    ):
        return self.events[-limit:]
episodic_memory = EpisodicMemory()