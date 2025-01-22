from src.managers.ingestion_manager import IngestionManager

class IngestionController:
    def __init__(self):
        self.ingestion_manager = IngestionManager()

    def process_pdf(self, file_path):
        """
        Processes a PDF file and extracts text.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Extracted text.
        """
        return self.ingestion_manager.extract_text(file_path)
