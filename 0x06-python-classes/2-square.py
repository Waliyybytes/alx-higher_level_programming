#!/usr/bin/python3
""" defining a class Square"""


class Square:
    """ class Square with

    Attribute __size(int) set to private
    It's crucial for a object like square

    """
    def __init__(self, size=0):
        """ Initializes an instance

        Args: size with integer validation

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
