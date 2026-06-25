from app.temporal.concept_timeline import (
    ConceptTimeline
)


class TemporalReasoner:

    @staticmethod
    def reason(
        concept
    ):

        events = (
            ConceptTimeline
            .get_timeline(
                concept
            )
        )

        if not events:
            return "unknown"

        last = events[-1]

        return last["event"]