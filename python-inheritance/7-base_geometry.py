#!/usr/bin/python3
"""
Module 7-base_geometry

Defines a BaseGeometry class with methods for area and integer validation.
"""


class BaseGeometry:
    """Base class for geometry objects.

    Provides methods that can be extended by subclasses.
    """

    def area(self):
        """Raise an exception since area is not implemented.

        Raises:
            Exception: Always with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the value (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
