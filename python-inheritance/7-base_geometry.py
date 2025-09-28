#!/usr/bin/python3
"""Module 7-base_geometry
Defines a class BaseGeometry.
"""


class BaseGeometry:
    """BaseGeometry class with unimplemented area method
    and an integer validator.
    """

    def area(self):
        """Raises an Exception with a standard message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): name of the value
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
