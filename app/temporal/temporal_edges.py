from datetime import datetime


class TemporalEdgeFactory:

    @staticmethod
    def create(
        source,
        relation,
        target
    ):

        return {
            "source": source,
            "relation": relation,
            "target": target,
            "timestamp":
            datetime.utcnow().isoformat()
        }