class ContradictionResolver:
    NEGATIONS = [
        "not",
        "never",
        "no",
        "none"
    ]
    @staticmethod
    def resolve(texts):
        contradictions = []
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                t1 = texts[i].lower()
                t2 = texts[j].lower()
                has_neg_1 = any(
                    word in t1
                    for word in ContradictionResolver.NEGATIONS
                )
                has_neg_2 = any(
                    word in t2
                    for word in ContradictionResolver.NEGATIONS
                )
                if has_neg_1 != has_neg_2:
                    contradictions.append(
                        {
                            "statement_1": texts[i],
                            "statement_2": texts[j],
                            "confidence": 0.8
                        }
                    )
        return contradictions