from abc import ABC, abstractmethod
import math


# 1. Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


# 2. Circle class
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("radius must be >= 0")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# 3. Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("width and height must be >= 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 4. shape_info function (duck typing: no isinstance checks!)
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# 5. Testing
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)
