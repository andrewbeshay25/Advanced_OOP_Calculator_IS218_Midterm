import os
import pytest
from pyfakefs.fake_filesystem_unittest import Patcher
import logging

from app.file_manager import FileManager

# Test Cases
@pytest.fixture
def fs():
    """Fixture to initialize pyfakefs."""
    with Patcher() as patcher:
        yield patcher.fs


def test_write_file_positive(fs, caplog):
    file_manager = FileManager("test_file.txt")
    
    with caplog.at_level(logging.INFO):
        file_manager.write_file("Hello, World!")

    # Check if the file exists in the fake filesystem
    assert fs.exists("test_file.txt")

    # Read the content to verify
    with open("test_file.txt", 'r') as file:
        content = file.read()
        assert content == "Hello, World!"
    
    # Check logging message, ensuring exact match
    assert "Successfully wrote to file: test_file.txt" in caplog.text

def test_read_file_positive(fs, caplog):
    fs.create_file("test_file.txt", contents="Hello, World!")

    file_manager = FileManager("test_file.txt")

    with caplog.at_level(logging.INFO):
        content = file_manager.read_file()

    assert content == "Hello, World!"

    # Check logging message for exact match
    assert "Successfully read from file: test_file.txt" in caplog.text

def test_read_file_negative(fs, caplog):
    file_manager = FileManager("non_existent_file.txt")

    with caplog.at_level(logging.ERROR):
        with pytest.raises(FileNotFoundError):
            file_manager.read_file()

    # Check logging for exact match
    assert "File not found: non_existent_file.txt" in caplog.text

def test_delete_file_negative(fs, caplog):
    file_manager = FileManager("non_existent_file.txt")

    with caplog.at_level(logging.WARNING):
        file_manager.delete_file()  # This should log a warning without raising an error

    # Check logging for exact match
    assert "File not found for deletion: non_existent_file.txt" in caplog.text
