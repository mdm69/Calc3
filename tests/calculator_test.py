"""Testing the Calculator"""
from calc.main import Calculator


def test_calculator_add_static():
    """ testing calc for addition """
    result = Calculator.add_numbers(1, 2)
    assert result == 3


def test_calculator_subtract_result():
    """ testing calc for subtraction """
    result = Calculator.subtract_numbers(3, 2)
    assert result == 1


def test_calculator_multiplication_result():
    """ testing calc for multiplication """
    result = Calculator.multiplication_numbers(3, 2)
    assert result == 6


def test_calculator_division_result():
    """ testing calc for division """
    result = Calculator.division_numbers(4, 2)
    assert result == 2
