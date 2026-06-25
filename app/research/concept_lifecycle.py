from datetime import datetime


class ConceptLifecycle:

    concepts = {}

    @classmethod
    def register(
        cls,
        concept
    ):

        if concept not in cls.concepts:

            cls.concepts[concept] = {
                "concept": concept,
                "birth_date": datetime.utcnow(),
                "mentions": 1,
                "confidence": 1.0,
                "last_seen": datetime.utcnow()
            }

        else:

            cls.concepts[concept][
                "mentions"
            ] += 1

            cls.concepts[concept][
                "last_seen"
            ] = datetime.utcnow()

        return cls.concepts[concept]

    @classmethod
    def get_all(cls):

        return list(
            cls.concepts.values()
        )