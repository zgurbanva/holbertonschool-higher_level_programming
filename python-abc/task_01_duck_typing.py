from abc import ABC, abstractmethod
import math


# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        # Instead of raising error, store absolute value
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        # Instead of raising error, store absolute values
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# shape_info function (duck typing)
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing
if __name__ == "__main__":
    # Negative Circle
    circle_negative = Circle(-5)
    print("Circle with negative radius:")
    shape_info(circle_negative)

    # Negative Rectangle
    rect_negative = Rectangle(-4, -6)
    print("\nRectangle with negative dimensions:")
    shape_info(rect_negative)
