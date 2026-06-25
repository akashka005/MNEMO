class ConceptTimeline:

    timelines = {}

    @classmethod
    def add_event(
        cls,
        concept,
        event
    ):

        if concept not in cls.timelines:

            cls.timelines[concept] = []

        cls.timelines[concept].append(
            event
        )

    @classmethod
    def get_timeline(
        cls,
        concept
    ):

        return cls.timelines.get(
            concept,
            []
        )