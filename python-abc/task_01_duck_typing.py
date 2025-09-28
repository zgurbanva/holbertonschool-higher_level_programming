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


# 2) Circle: allow negative radius but compute with abs so it doesn't crash
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
        # Signed area (e.g., -4 * 7 = -28) to match the test expectation
        return self.width * self.height

    def perimeter(self):
        # Perimeter should be non-negative; use absolute lengths
        return 2 * (abs(self.width) + abs(self.height))


# 4) Duck-typed utility (no isinstance checks)
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# 5) Quick manual run (optional)
if __name__ == "__main__":
    # Circle negative radius should not crash
    c = Circle(-5)
    print("Circle (radius = -5):")
    shape_info(c)

    # Rectangle negative dimension should yield signed area
    r = Rectangle(-4, 7)
    print("\nRectangle (width = -4, height = 7):")
    shape_info(r)
