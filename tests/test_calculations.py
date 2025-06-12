import pytest
from app.calculator import Calculator
from app.calculation import Calculation

def test_calculation_str():
    calc = Calculation(2, 3, "add", 5)
    assert str(calc) == "2 add 3 = 5"

def test_calculator_addition():
    c = Calculator()
    result = c.perform_operation("add", 2, 3)
    assert result == 5
    assert len(c.history) == 1
    assert str(c.history[0]) == "2 add 3 = 5"

def test_calculator_subtraction():
    c = Calculator()
    result = c.perform_operation("subtract", 5, 2)
    assert result == 3

def test_calculator_multiplication():
    c = Calculator()
    result = c.perform_operation("multiply", 4, 3)
    assert result == 12

def test_calculator_division():
    c = Calculator()
    result = c.perform_operation("divide", 10, 2)
    assert result == 5

def test_calculator_divide_by_zero():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.perform_operation("divide", 10, 0)

def test_invalid_operation():
    c = Calculator()
    with pytest.raises(ValueError):
        c.perform_operation("mod", 2, 3)

