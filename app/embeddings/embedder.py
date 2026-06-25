from typing import List
from sentence_transformers import SentenceTransformer
from app.config.settings import settings

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(
            settings.EMBED_MODEL
        )
    def embed_text(
        self,
        text: str
    ) -> List[float]:
        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )
        return embedding.tolist()
    def embed_batch(
        self,
        texts: list[str]
    ) -> list[list[float]]:
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )
        return embeddings.tolist()
    def embedding_dimension(self) -> int:
        return self.model.get_embedding_dimension()
embedder = Embedder()