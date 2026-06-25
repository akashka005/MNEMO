from typing import Dict, List

class EmbeddingCache:
    def __init__(self):
        self.cache: Dict[
            str,
            List[float]
        ] = {}
    def get(
        self,
        text: str
    ):
        return self.cache.get(text)
    def set(
        self,
        text: str,
        embedding: List[float]
    ):
        self.cache[text] = embedding
    def exists(
        self,
        text: str
    ) -> bool:
        return text in self.cache
    def clear(self):
        self.cache.clear()
embedding_cache = EmbeddingCache()