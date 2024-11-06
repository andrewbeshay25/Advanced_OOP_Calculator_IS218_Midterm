from typing import List, Union

from app.calculation import Calculation
from app.operations import Number

# Command pattern for executing operations
class OperationCommand:
    def __init__(self, operation: Calculation) -> None:
        self.operation = operation

    def execute(self) -> Number:
        return self.operation.compute()

class HistoryManager:
    """
    Manages the history of executed operations.

    This class allows adding to, retrieving, and undoing from a history of operations.
    It stores a list of `OperationCommand` objects representing each calculation.

    Attributes:
    _history (List[OperationCommand]): List of operations executed.
    """

    def __init__(self) -> None:
        """Initializes the history manager with an empty history list."""
        self._history: List[OperationCommand] = []

    def add_to_history(self, operation: 'OperationCommand') -> None:
        """
        Add a new operation to the history.

        Args:
        operation (OperationCommand): The operation to add to the history.
        """
        self._history.append(operation)

    def get_latest(self, n: int = 1) -> List['OperationCommand']:
        """
        Get the latest n operations from the history.

        Args:
        n (int): The number of recent operations to retrieve. Defaults to 1.

        Returns:
        List[OperationCommand]: A list of the latest operations.
        """
        return self._history[-n:]

    def clear_history(self) -> None:
        """Clear the entire history."""
        self._history.clear()

    def get_full_history(self) -> List['OperationCommand']:
        """
        Retrieve the entire operation history.

        Returns:
        List[OperationCommand]: The full list of operations.
        """
        return self._history

    def undo_last(self) -> Union['OperationCommand', None]:
        """
        Undo the last operation in the history.

        Returns:
        Union[OperationCommand, None]: The last operation that was undone, or None if history is empty.
        """
        if self._history:
            return self._history.pop()
        return None