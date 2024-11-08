import os
import logging
from typing import Any

def setup_logging(level: int = logging.INFO, log_filename: str = None) -> None:
  # Set up the root logger
    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logging.info(f"Started logging session -> {log_filename}")

class FileManager:
    def __init__(self, filename: str, log_filename: str = "app.log") -> None:
        self.filename = filename
        setup_logging(log_filename=log_filename)  # Separate log file


    def write_file(self, data: str) -> None:
        """Write data to a file.
        
        Args:
            data (str): The data to write to the file.
        
        Raises:
            IOError: If an I/O error occurs during writing.
        """
        try:
            with open(self.filename, 'w') as file:
                file.write(data)
            logging.info(f"Successfully wrote to file: {self.filename}")
        except IOError as e:
            logging.error(f"Failed to write to file '{self.filename}'. Error: {e}")
            raise

    def read_file(self) -> str:
        """Read data from a file.
        
        Returns:
            str: The content of the file.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If an I/O error occurs during reading.
        """
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            logging.info(f"Successfully read from file: {self.filename}")
            return content
        except FileNotFoundError:
            logging.error(f"File not found: {self.filename}")
            raise
        except IOError as e:
            logging.error(f"Failed to read from file '{self.filename}'. Error: {e}")
            raise

    def delete_file(self) -> None:
        """Delete the file, if it exists.
        
        Raises:
            OSError: If an error occurs during deletion.
        """
        try:
            os.remove(self.filename)
            logging.info(f"Successfully deleted file: {self.filename}")
        except FileNotFoundError:
            logging.warning(f"File not found for deletion: {self.filename}")
        except OSError as e:
            logging.error(f"Failed to delete file '{self.filename}'. Error: {e}")
            raise
