import os
import pytest
import pandas as pd
from pyfakefs.fake_filesystem_unittest import Patcher
from data.csv_manager import CsvManager

# Set the environment variable for the test
os.environ["CSV_PATH"] = "operations_log.csv"

@pytest.fixture
def csv_manager(fs):
    """Fixture to initialize CsvManager with a fake filesystem."""
    with Patcher() as patcher:
        patcher.fs.create_file("operations_log.csv")
        manager = CsvManager()  # CsvManager now uses the environment variable
        yield manager

def test_initialize_csv(csv_manager):
    """Test that the CSV file is initialized with headers if it doesn't exist."""
    df = pd.read_csv("operations_log.csv")
    expected_columns = ["operation", "a", "b", "result"]
    assert list(df.columns) == expected_columns

def test_log_operation(csv_manager):
    """Test logging an operation to the CSV file."""
    csv_manager.log_operation("add", 2, 3, 5)
    df = pd.read_csv("operations_log.csv")
    assert len(df) == 1
    assert df.iloc[0]["operation"] == "add"
    assert df.iloc[0]["a"] == 2
    assert df.iloc[0]["b"] == 3
    assert df.iloc[0]["result"] == 5

def test_read_operations(csv_manager):
    """Test reading operations from the CSV file."""
    data = {
        "operation": ["add", "multiply"],
        "a": [2, 4],
        "b": [3, 5],
        "result": [5, 20]
    }
    pd.DataFrame(data).to_csv("operations_log.csv", index=False)
    df = csv_manager.read_operations()
    assert len(df) == 2
    assert df.iloc[0]["operation"] == "add"
    assert df.iloc[1]["operation"] == "multiply"

def test_log_multiple_operations(csv_manager):
    """Test logging multiple operations to the CSV file."""
    csv_manager.log_operation("subtract", 8, 3, 5)
    csv_manager.log_operation("divide", 10, 2, 5)
    df = pd.read_csv("operations_log.csv")
    assert len(df) == 2
    assert df.iloc[0]["operation"] == "subtract"
    assert df.iloc[1]["operation"] == "divide"
