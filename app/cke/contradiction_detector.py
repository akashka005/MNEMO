class ContradictionDetector:
    NEGATIONS = [
        "not",
        "never",
        "no",
        "none",
        "without"
    ]
    @staticmethod
    def detect(
        texts: list[str]
    ):
        contradictions = []
        for i in range(
            len(texts)
        ):
            for j in range(
                i + 1,
                len(texts)
            ):
                t1 = texts[i].lower()
                t2 = texts[j].lower()
                has_negation = any(
                    n in t1 or n in t2
                    for n in (
                        ContradictionDetector
                        .NEGATIONS
                    )
                )
                shared = (
                    len(
                        set(t1.split())
                        &
                        set(t2.split())
                    )
                )
                if (
                    has_negation
                    and shared >= 2
                ):
                    contradictions.append(
                        {
                            "statement_1": texts[i],
                            "statement_2": texts[j]
                        }
                    )
        return contradictions