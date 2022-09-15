#!/usr/bin/python3
""" defining a class Square"""


class Square:
    """
    Square Blueprint
    Attributes:
        __size(int): size of side of a sqaure
    Methods:
        __init__
        area

    """
    def __init__(self, size=0):
        """
        Initializes the square
        Args:
            size(int)
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Evaluates the Area of the square
        Args:
            None
        Returns:
            result of area calculated (int)
        """
        return self.__size ** 2
