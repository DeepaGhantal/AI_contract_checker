from langchain.embeddings import HuggingFaceEmbeddings
from src.configuration.config import Config

class EmbeddingController:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def generate_embedding(self, text):
        """
        Generate an embedding for a single text input.

        Args:
            text (str): The input text.

        Returns:
            list: Embedding vector.
        """
        return self.model.embed_query(text)

    def generate_embeddings(self, chunks):
        """
        Generate embeddings for a list of text chunks.

        Args:
            chunks (list): A list of text chunks.

        Returns:
            list: List of embedding vectors.
        """
        return [self.generate_embedding(chunk) for chunk in chunks]
