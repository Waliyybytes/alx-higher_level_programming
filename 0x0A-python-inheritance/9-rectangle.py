#!/usr/bin/python3
"""
    Base Geometry module creation with subclass Rectangle

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """ attributes instantiation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """evaluates area of class Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representattion of Rectangle"""
        return "Rectangle {:d}/{:d}".format(self.__width, self.__height)
