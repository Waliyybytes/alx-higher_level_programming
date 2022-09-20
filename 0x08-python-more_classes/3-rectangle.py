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

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Evaluates the Area of the rectangle
        Args:
            None
        Returns:
            result of area calculated (int)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Evaluates the perimeter of the rectangle
        Args:
            None
        Returns:
            result of area calculated (int)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints a square instance
        A string representation of the   square
        """
        rep = ""
        a = self.__width
        b = self.__height
        if a == 0 or b == 0:
            return ''
        sqr = "#" * a
        for i in range(b):
            rep += sqr
            if i != b - 1:
                rep += '\n'
        return rep
