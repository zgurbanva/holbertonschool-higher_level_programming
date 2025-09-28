#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle defines a rectangle with validated private attributes.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated width and height.

        Args:
            width (int): The rectangle's width (must be > 0).
            height (int): The rectangle's height (must be > 0).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
