#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Square class that defines a square by its size.
    The size attribute is private so that validation logic
    can be safely added in later tasks.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value checks here).
        """
        self.__size = size

