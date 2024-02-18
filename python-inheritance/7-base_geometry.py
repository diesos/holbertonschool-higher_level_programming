"""Defines 'BaseGeometry' class with an abstract 'area()' method and 'integer_validator()' method."""


class BaseGeometry:
    """Initializes an instance of 'BaseGeometry'."""

    def __init__(self):
        pass

    """Raises an exception as 'area()' is not implemented in this base class."""

    def area(self):
        raise Exception("area() is not implemented")

    """Validates if 'value' is an integer greater than 0."""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
