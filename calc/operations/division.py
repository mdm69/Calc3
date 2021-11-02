""""Division Class"""


class Division:
    """ dividing two numbers """

    @staticmethod
    def division(value_a, value_b):
        """ divides value_a and value_b """
        try:
            return value_a // value_b
        except ZeroDivisionError:
            return None
