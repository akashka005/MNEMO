from app.cke.result import CKEResult
from app.cke.result import CKEOperation
from app.embeddings.similarity import SimilarityService
from app.config.settings import settings

class CKEClassifier:
    @staticmethod
    def classify(
        source_embedding,
        target_embedding
    ) -> CKEResult:
        score = SimilarityService.cosine_similarity(
            source_embedding,
            target_embedding
        )
        if score >= settings.MERGE_THRESHOLD:
            return CKEResult(
                operation=CKEOperation.MERGE,
                confidence=float(score),
                explanation="High semantic overlap."
            )
        if score >= settings.EXTEND_THRESHOLD:
            return CKEResult(
                operation=CKEOperation.EXTEND,
                confidence=float(score),
                explanation="Related concept."
            )
        if score <= settings.CONFLICT_THRESHOLD:
            return CKEResult(
                operation=CKEOperation.CONFLICT,
                confidence=1.0 - float(score),
                explanation="Potential contradiction."
            )
        return CKEResult(
            operation=CKEOperation.EMERGE,
            confidence=float(score),
            explanation="Weakly related knowledge."
        )