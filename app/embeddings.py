from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingModel:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Local embedding model.
        Loaded once at startup.
        """
        self.model = SentenceTransformer(model_name)

    def encode(self, text: str) -> np.ndarray:
        """
        Convert text into a dense embedding vector.
        """
        if not text:
            return np.zeros(self.model.get_sentence_embedding_dimension())

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        return embedding
