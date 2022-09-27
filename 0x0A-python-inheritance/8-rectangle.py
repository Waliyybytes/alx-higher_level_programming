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
