from src.managers.chunk_manager import ChunkManager
from src.configuration.config import Config

class ChunkController:
    def __init__(self):
        self.chunk_manager = ChunkManager()

    def split_text_into_chunks(self, text):
        """
        Splits the input text into smaller chunks.

        Args:
            text (str): The full text.

        Returns:
            list: A list of text chunks.
        """
        return self.chunk_manager.split_text(text, Config.CHUNK_SIZE, Config.CHUNK_OVERLAP)
