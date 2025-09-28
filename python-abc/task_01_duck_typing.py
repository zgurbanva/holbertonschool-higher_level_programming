#!/usr/bin/env python3
"""
Duck typing with abstract base classes:
Define Shape as an abstract class and implement Circle and Rectangle.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        # Zero is allowed; negatives are not
        if radius < 0:
            raise ValueError("radius must be >= 0")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        # Zero is allowed; negatives are not
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        # If either dimension is zero, perimeter is the usual 2*(w+h) which
        # correctly becomes 0 only when both are zero.
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of the given shape.
    Relies on duck typing (expects shape to have area() and perimeter()).
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
