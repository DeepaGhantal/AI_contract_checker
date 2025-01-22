from langchain.text_splitter import RecursiveCharacterTextSplitter

class ChunkManager:
    def split_text(self, text, chunk_size, chunk_overlap):
        """
        Splits text into smaller overlapping chunks.

        Args:
            text (str): The input text to split.
            chunk_size (int): The size of each chunk.
            chunk_overlap (int): The overlap between consecutive chunks.

        Returns:
            list: A list of text chunks.
        """
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return splitter.split_text(text)
