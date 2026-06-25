from app.temporal.concept_timeline import (
    ConceptTimeline
)


class TemporalGraph:

    @staticmethod
    def add_concept(
        concept
    ):

        ConceptTimeline.add_event(
            concept,
            {
                "event":
                "created"
            }
        )

    @staticmethod
    def evolve(
        concept,
        change
    ):

        ConceptTimeline.add_event(
            concept,
            {
                "event":
                "evolved",
                "change":
                change
            }
        )

    @staticmethod
    def contradict(
        concept
    ):

        ConceptTimeline.add_event(
            concept,
            {
                "event":
                "contradicted"
            }
        )

    @staticmethod
    def obsolete(
        concept
    ):

        ConceptTimeline.add_event(
            concept,
            {
                "event":
                "obsolete"
            }
        )