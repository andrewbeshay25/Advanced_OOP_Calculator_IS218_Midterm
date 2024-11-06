import pytest
from app.calculation import Addition, Subtraction, Multiplication, Division  # Assuming your classes are in 'calculation' module

# Parameterized test for Addition with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2), (2, 3, 5), (-1, -1, -2), (0, 0, 0)
])
def test_addition(a, b, expected):
    '''Test for addition operation'''
    operation = Addition.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Addition: {a} + {b} = {expected}"
    assert repr(operation) == f"Addition(a={a}, b={b}, result={expected})"

# Parameterized test for Subtraction with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0), (5, 3, 2), (-1, -1, 0), (0, 5, -5)
])
def test_subtraction(a, b, expected):
    '''Test for subtraction operation'''
    operation = Subtraction.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Subtraction: {a} - {b} = {expected}"
    assert repr(operation) == f"Subtraction(a={a}, b={b}, result={expected})"

# Parameterized test for Multiplication with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4), (3, 5, 15), (0, 5, 0), (-1, 1, -1)
])
def test_multiplication(a, b, expected):
    '''Test for multiplication operation'''
    operation = Multiplication.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Multiplication: {a} * {b} = {expected}"
    assert repr(operation) == f"Multiplication(a={a}, b={b}, result={expected})"

# Parameterized test for Division with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 1), (10, 5, 2), (9, 3, 3), (7, 2, 3.5)
])
def test_division(a, b, expected):
    '''Test for division operation'''
    operation = Division.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Division: {a} / {b} = {expected}"
    assert repr(operation) == f"Division(a={a}, b={b}, result={expected})"

# Test for division by zero exception
def test_division_by_zero_exception():
    '''Test for division by zero exception'''
    operation = Division.create(10, 0)
    with pytest.raises(ZeroDivisionError):
        operation.compute()