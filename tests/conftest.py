# Fixture to create a Calculator instance
import sys
import pexpect
import pytest

from app.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator.create()

@pytest.fixture
def repl():
    """Fixture to start the REPL application."""
    # Path to the main.py script
    script = 'main.py'

    # Start the REPL application
    child = pexpect.spawn(sys.executable + f' {script}', encoding='utf-8', timeout=5)
    child.expect('Welcome to the Calculator REPL.*')
    yield child
    child.terminate()