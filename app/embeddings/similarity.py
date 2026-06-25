from typing import List
import numpy as np

class SimilarityService:
    @staticmethod
    def cosine_similarity(
        vector_a: List[float],
        vector_b: List[float]
    ) -> float:
        a = np.array(vector_a)
        b = np.array(vector_b)
        denominator = (
            np.linalg.norm(a)
            *
            np.linalg.norm(b)
        )
        if denominator == 0:
            return 0.0
        similarity = np.dot(a, b) / denominator
        return float(similarity)
    @staticmethod
    def euclidean_distance(
        vector_a: List[float],
        vector_b: List[float]
    ) -> float:
        a = np.array(vector_a)
        b = np.array(vector_b)
        return float(
            np.linalg.norm(a - b)
        )
    @staticmethod
    def is_similar(
        vector_a: List[float],
        vector_b: List[float],
        threshold: float = 0.85
    ) -> bool:
        score = SimilarityService.cosine_similarity(
            vector_a,
            vector_b
        )
        return score >= threshold
    @staticmethod
    def similarity_score(
        vector_a: List[float],
        vector_b: List[float]
    ) -> float:
        return SimilarityService.cosine_similarity(
            vector_a,
            vector_b
        )