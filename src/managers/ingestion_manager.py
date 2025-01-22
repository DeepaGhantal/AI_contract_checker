from PyPDF2 import PdfReader

class IngestionManager:
    def extract_text(self, file_path):
        """
        Extracts text from a PDF file.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Extracted text.
        """
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text: {e}")
            return ""
