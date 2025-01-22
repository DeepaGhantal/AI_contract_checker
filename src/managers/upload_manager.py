import os

class UploadManager:
    def upload_file(self, file_path):
        """
        Mock method for uploading a file.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: Upload status.
        """
        if os.path.exists(file_path):
            print(f"File '{file_path}' uploaded successfully.")
            return "Upload successful"
        else:
            print(f"File '{file_path}' not found.")
            return "Upload failed"
