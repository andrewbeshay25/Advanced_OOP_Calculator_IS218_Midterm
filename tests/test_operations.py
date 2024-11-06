''' My Calculator Test'''
import pytest
from app.operations import addition, division, multiplication, subtraction


# Parameterized test for addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2), (2, 3, 5), (-1, -1, -2), (0, 0, 0)
])
def test_addition(a, b, expected):
    '''Addition function'''
    assert addition(a, b) == expected

# Parameterized test for subtraction
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0), (5, 3, 2), (-1, -1, 0), (0, 5, -5)
])
def test_subtraction(a, b, expected):
    '''Subtraction function'''
    assert subtraction(a, b) == expected

# Parameterized test for multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4), (3, 5, 15), (0, 5, 0), (-1, 1, -1)
])
def test_multiplication(a, b, expected):
    '''Multiplication function'''
    assert multiplication(a, b) == expected

# Parameterized test for division
@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 1), (10, 5, 2), (9, 3, 3)
])
def test_division(a, b, expected):
    '''Division function'''
    assert division(a, b) == expected

# Test for division by zero exception
def test_division_by_zero_exception():
    '''Division function testing that I get the exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)