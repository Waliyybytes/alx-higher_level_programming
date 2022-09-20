#!/usr/bin/python3
"""
    Real definition of rectangle

"""

class Rectangle:
    """
    Real definition of rectangle parameters

    Args:
        width, height ----private attributes
    """

    def __init__(self, width=0, height=0):
        """ Instantiates the class attributes"""

        self.size = size
        self.position = position

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__height = value
