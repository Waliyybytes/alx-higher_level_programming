#!/usr/bin/python3
"""
    Base Geometry module creation with subclass Rectangle

"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        Rectangle class inherits from BaseGeometry
    """
    def __init__(self, size):
        """ attributes instantiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ evaluates the area of a square"""
        return self.__size ** 2
