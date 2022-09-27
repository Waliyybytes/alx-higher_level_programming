#!/usr/bin/python3
"""
    Base Geometry module creation with subclass Rectangle

"""


class BaseGeometry():
    """
        Creattion of class BaseGeometry

    """
    def area(self):
        """
            Method to implement area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            To validate the attribute 'value'

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
