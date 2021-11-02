""" Calling all operations"""

from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.division import Division
from calc.operations.multiplication import Multiplication


class Calculator:
    """ This is the Calculator class """

    # default constructor

    def __init__(self):
        self.result = 0

    def get_result(self):
        """ Get Result of Calculation """
        return self.result

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adding two numbers """
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtracting number from result """
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def division_numbers(value_a, value_b):
        """ dividing two numbers """
        return Division.division(value_a, value_b)

    @staticmethod
    def multiplication_numbers(value_a, value_b):
        """ multiply two numbers """
        return Multiplication.multiplication(value_a, value_b)
