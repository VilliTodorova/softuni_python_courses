from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius: float):
        self.__radius = radius

    def calculate_area(self):
        return pi * pow(self.__radius, 2)

    def calculate_perimeter(self):
        return pi * self.__radius * 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
