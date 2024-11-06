import pytest
from unittest.mock import Mock
from app.calculation import Calculation
from app.history_manager import OperationCommand, HistoryManager  # Assuming HistoryManager is in 'history_manager'

# Test OperationCommand
def test_operation_command_execution():
    """
    Test that OperationCommand calls the compute method on the given operation.
    """
    # Create a mock Calculation object
    mock_operation = Mock(spec=Calculation)
    mock_operation.compute.return_value = 10  # Set compute return value

    # Create an OperationCommand with the mock operation
    command = OperationCommand(mock_operation)

    # Execute the command and assert that compute is called and returns the expected result
    result = command.execute()
    assert result == 10
    mock_operation.compute.assert_called_once()  # Ensure compute() was called exactly once

# Test HistoryManager
def test_add_to_history():
    """
    Test adding an operation to the history.
    """
    # Create a mock OperationCommand
    mock_command = Mock(spec=OperationCommand)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add the mock command to history and verify that it is stored correctly
    history_manager.add_to_history(mock_command)
    assert len(history_manager.get_full_history()) == 1
    assert history_manager.get_full_history()[0] == mock_command

def test_get_latest():
    """
    Test retrieving the latest n operations from history.
    """
    # Create mock OperationCommand objects
    mock_command_1 = Mock(spec=OperationCommand)
    mock_command_2 = Mock(spec=OperationCommand)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add two commands to history
    history_manager.add_to_history(mock_command_1)
    history_manager.add_to_history(mock_command_2)

    # Retrieve the latest operation
    latest_operation = history_manager.get_latest(1)
    assert len(latest_operation) == 1
    assert latest_operation[0] == mock_command_2

    # Retrieve the latest 2 operations
    latest_two_operations = history_manager.get_latest(2)
    assert len(latest_two_operations) == 2
    assert latest_two_operations == [mock_command_1, mock_command_2]

def test_clear_history():
    """
    Test clearing the history.
    """
    # Create mock OperationCommand objects
    mock_command_1 = Mock(spec=OperationCommand)
    mock_command_2 = Mock(spec=OperationCommand)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add two commands to history
    history_manager.add_to_history(mock_command_1)
    history_manager.add_to_history(mock_command_2)

    # Clear the history
    history_manager.clear_history()

    # Assert that the history is now empty
    assert len(history_manager.get_full_history()) == 0

def test_undo_last():
    """
    Test undoing the last operation in history.
    """
    # Create mock OperationCommand objects
    mock_command_1 = Mock(spec=OperationCommand)
    mock_command_2 = Mock(spec=OperationCommand)

    # Create a HistoryManager instance
    history_manager = HistoryManager()

    # Add two commands to history
    history_manager.add_to_history(mock_command_1)
    history_manager.add_to_history(mock_command_2)

    # Undo the last operation and verify the result
    last_operation = history_manager.undo_last()
    assert last_operation == mock_command_2
    assert len(history_manager.get_full_history()) == 1

    # Undo the next operation
    last_operation = history_manager.undo_last()
    assert last_operation == mock_command_1
    assert len(history_manager.get_full_history()) == 0

    # Ensure that undoing when the history is empty returns None
    last_operation = history_manager.undo_last()
    assert last_operation is None