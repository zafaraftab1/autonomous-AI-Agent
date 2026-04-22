# Purpose: Converts text into vector embeddings (for FAISS search)

from sentence_transformers import SentenceTransformer

# Lightweight and fast model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    """
    Convert text into vector embedding
    """
    return model.encode(text)