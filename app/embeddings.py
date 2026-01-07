from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def encode(self, text: str) -> np.ndarray:
        if not text.strip():
            return np.zeros(384)
        return self.model.encode(text, normalize_embeddings=True)
