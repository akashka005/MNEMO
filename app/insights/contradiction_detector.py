class ContradictionDetector:

    NEGATIONS = [
        "not",
        "never",
        "cannot",
        "false"
    ]

    @staticmethod
    def detect(nodes):

        contradictions = []

        for node in nodes:

            text = (
                node.get("text", "")
                .lower()
            )

            if any(
                word in text
                for word in (
                    ContradictionDetector
                    .NEGATIONS
                )
            ):
                contradictions.append(
                    node
                )

        return contradictions