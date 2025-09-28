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

        Args:
            radius (float or int): The radius of the circle (must be > 0).

        Raises:
            TypeError: If radius is not a number.
            ValueError: If radius <= 0.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be greater than 0")
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

        Args:
            width (int or float): The width of the rectangle (must be > 0).
            height (int or float): The height of the rectangle (must be > 0).

        Raises:
            TypeError: If width or height is not a number.
            ValueError: If width <= 0 or height <= 0.
        """
        for name, value in (("width", width), ("height", height)):
            if not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be a number")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
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
