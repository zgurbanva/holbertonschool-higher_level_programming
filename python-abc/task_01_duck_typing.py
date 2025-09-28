#!/usr/bin/env python3
"""
This module defines an abstract Shape class with Circle and Rectangle
implementations, and a function shape_info that demonstrates duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    Requires subclasses to implement area() and perimeter().
    """

    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape implementation with radius.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape implementation with width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of the given shape.

    Args:
        shape: Any object with area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
