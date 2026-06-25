class ReRanker:
    @staticmethod
    def rerank(
        candidates
    ):
        for item in candidates:
            similarity = item.get(
                "score",
                0.0
            )
            confidence = item.get(
                "confidence",
                1.0
            )
            item["final_score"] = (
                similarity * 0.8 +
                confidence * 0.2
            )
        candidates.sort(
            key=lambda x:
            x["final_score"],
            reverse=True
        )
        return candidates