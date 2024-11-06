from typing import List, Union
from app.calculation import Calculation
from app.history_manager import HistoryManager, OperationCommand
from app.operations import Number


class Calculator:
    """
    The Calculator class ties together operations and their history.
    
    This class allows performing operations, managing the operation history, and undoing actions.

    Attributes:
    history_manager (HistoryManager): Manages the history of operations.
    """

    def __init__(self) -> None:
        """Initializes the Calculator with a history manager."""
        self.history_manager = HistoryManager()

    def perform_operation(self, operation: 'Calculation') -> Number:
        """
        Perform the calculation and store it in history.

        Args:
        operation (Calculation): The calculation to perform.

        Returns:
        Number: The result of the calculation.
        """
        command = OperationCommand(operation)
        result = command.execute()
        self.history_manager.add_to_history(command)
        return result

    def get_history(self) -> List['OperationCommand']:
        """
        Get the full history of performed operations.

        Returns:
        List[OperationCommand]: The list of all performed operations.
        """
        return self.history_manager.get_full_history()

    def undo(self) -> Union['OperationCommand', None]:
        """
        Undo the last operation.

        Returns:
        Union[OperationCommand, None]: The last operation that was undone, or None if history is empty.
        """
        return self.history_manager.undo_last()

    def clear_history(self) -> None:
        """Clear the entire calculator history."""
        self.history_manager.clear_history()