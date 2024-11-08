import pandas as pd
import os
import logging

class CsvManager:
    def __init__(self, filename: str = None) -> None:
        """Initialize with a CSV filename from env variable if not provided."""
        self.filename = filename or os.getenv("CSV_PATH", "data/operations_log.csv")
        
        # Check if the file exists; if not, create it with headers
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            self.initialize_csv()

    def initialize_csv(self) -> None:
        """Create the CSV file with headers if it doesn't exist."""
        df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        df.to_csv(self.filename, index=False)
        logging.debug("Initialized CSV with headers.")

    def log_operation(self, operation: str, a: float, b: float, result: float) -> None:
        """Log a new operation to the CSV file."""
        new_entry = {"operation": operation, "a": a, "b": b, "result": result}
        df = pd.DataFrame([new_entry])
        df.to_csv(self.filename, mode="a", header=False, index=False)
        logging.debug(f"Logged operation: {operation} with a={a}, b={b}, result={result}.")

    def read_operations(self) -> pd.DataFrame:
        """Read all operations from the CSV file and return as a DataFrame."""
        try:
            df = pd.read_csv(self.filename)
            logging.debug(f"Read {len(df)} operations from CSV.")
            return df
        except pd.errors.EmptyDataError:
            logging.warning("Attempted to read from an empty CSV file.")
            return pd.DataFrame(columns=["operation", "a", "b", "result"])
