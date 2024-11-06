import pytest
from unittest.mock import Mock
from app.calculation import Calculation
from app.calculator import Calculator
from app.history_manager import OperationCommand


def test_perform_operation():
    """
    Test that Calculator performs an operation and stores it in the history.
    """
    # Create a mock Calculation object
    mock_operation = Mock(spec=Calculation)
    mock_operation.compute.return_value = 15  # Set compute return value
    
    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform the operation and assert the result
    result = calculator.perform_operation(mock_operation)
    assert result == 15
    mock_operation.compute.assert_called_once()  # Ensure compute() was called once

    # Check that the operation was added to the history
    history = calculator.get_history()
    assert len(history) == 1
    assert isinstance(history[0], OperationCommand)


def test_get_history():
    """
    Test that Calculator retrieves the full history of operations.
    """
    # Create two mock Calculation objects
    mock_operation_1 = Mock(spec=Calculation)
    mock_operation_1.compute.return_value = 10
    mock_operation_2 = Mock(spec=Calculation)
    mock_operation_2.compute.return_value = 20

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform two operations
    calculator.perform_operation(mock_operation_1)
    calculator.perform_operation(mock_operation_2)

    # Retrieve the full history
    history = calculator.get_history()
    assert len(history) == 2  # Two operations should be in the history

    # Ensure the history contains OperationCommand objects
    assert isinstance(history[0], OperationCommand)
    assert isinstance(history[1], OperationCommand)


def test_undo():
    """
    Test that Calculator can undo the last operation.
    """
    # Create two mock Calculation objects
    mock_operation_1 = Mock(spec=Calculation)
    mock_operation_1.compute.return_value = 10
    mock_operation_2 = Mock(spec=Calculation)
    mock_operation_2.compute.return_value = 20

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform two operations
    calculator.perform_operation(mock_operation_1)
    calculator.perform_operation(mock_operation_2)

    # Undo the last operation and check that the correct operation was undone
    last_operation = calculator.undo()
    assert last_operation.operation == mock_operation_2

    # Check that the history now contains only the first operation
    history = calculator.get_history()
    assert len(history) == 1
    assert history[0].operation == mock_operation_1

    # Undo the first operation
    last_operation = calculator.undo()
    assert last_operation.operation == mock_operation_1

    # Check that the history is now empty
    assert len(calculator.get_history()) == 0

    # Undo when history is empty
    last_operation = calculator.undo()
    assert last_operation is None


def test_clear_history():
    """
    Test that Calculator can clear the history.
    """
    # Create two mock Calculation objects
    mock_operation_1 = Mock(spec=Calculation)
    mock_operation_1.compute.return_value = 10
    mock_operation_2 = Mock(spec=Calculation)
    mock_operation_2.compute.return_value = 20

    # Create an instance of the Calculator
    calculator = Calculator()

    # Perform two operations
    calculator.perform_operation(mock_operation_1)
    calculator.perform_operation(mock_operation_2)

    # Clear the history
    calculator.clear_history()

    # Check that the history is empty
    history = calculator.get_history()
    assert len(history) == 0