# Purpose: Store and retrieve embeddings using FAISS

import faiss
import numpy as np
import self
from app.memory.embeddings import get_embedding

class VectorStore:
    def __init__(self):
        self.dimension = 384  # depends on embedding model
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []  # stores original text

    def add(self, text: str, source: str = ""):
        emb = get_embedding(text)

        self.index.add(np.array([emb]).astype("float32"))
        self.texts.append(text)
        self.metadata.append(source)

    def search(self, query: str, k=3):
        """
        Retrieve top-k similar texts
        """
        query_embedding = get_embedding(query)
        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"), k
        )

        results = [self.texts[i] for i in indices[0] if i < len(self.texts)]
        return results


# Global instance (simple approach)
vector_store = VectorStore()
# ADD this: metadata storage

self.metadata = []  # store source info