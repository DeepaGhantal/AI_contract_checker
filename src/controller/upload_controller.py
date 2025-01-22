from src.managers.upload_manager import UploadManager

class UploadController:
    def __init__(self):
        self.upload_manager = UploadManager()

    def upload_file(self, file_path):
        """
        Upload a file to the server.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: Upload status.
        """
        return self.upload_manager.upload_file(file_path)
