# task_01_duck_typing.py
from abc import ABC, abstractmethod
import math


# 1) Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area (may be signed for some shapes)."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return the (non-negative) perimeter/circumference."""
        raise NotImplementedError


# 2) Circle: allow negative radius but compute with abs so it doesn’t crash
class Circle(Shape):
    def __init__(self, radius):
        # Do not raise; just store the raw value
        self.radius = radius

    def area(self):
        # Use absolute radius for a meaningful area
        r = abs(self.radius)
        return math.pi * (r ** 2)

    def perimeter(self):
        r = abs(self.radius)
        return 2 * math.pi * r


# 3) Rectangle: keep signed dimensions; area must be signed per tests
class Rectangle(Shape):
    def __init__(self, width, height):
        # Store as-is (tests expect signed area when a dimension is negative)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        # Always use abs for perimeter, since perimeter can’t be negative
        return 2 * (abs(self.width) + abs(self.height))


# 4) Duck typing function
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
