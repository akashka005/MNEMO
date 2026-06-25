import faiss
import numpy as np
from app.config.settings import settings

class FaissStore:
    def __init__(self):
        self.dimension = settings.EMBED_DIMENSION
        self.index = faiss.IndexFlatIP(
            self.dimension
        )
        self.node_ids = []
    def add(
        self,
        node_id: str,
        embedding
    ):
        vector = np.array(
            [embedding],
            dtype=np.float32
        )
        faiss.normalize_L2(vector)
        self.index.add(vector)
        self.node_ids.append(
            node_id
        )
    def search(
        self,
        embedding,
        top_k: int = 5
    ):
        if self.index.ntotal == 0:
            return []
        query = np.array(
            [embedding],
            dtype=np.float32
        )
        faiss.normalize_L2(query)
        scores, indices = self.index.search(
            query,
            top_k
        )
        results = []
        for score, idx in zip(
            scores[0],
            indices[0]
        ):
            if idx < 0:
                continue
            results.append(
                {
                    "node_id":
                        self.node_ids[idx],
                    "score":
                        float(score)
                }
            )
        return results
faiss_store = FaissStore()