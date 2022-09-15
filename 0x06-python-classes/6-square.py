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
    Property:
        size: to retrieve it and set it

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square
        Args:
            size(int)
        Returns:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if len(value) == 2 \
                        and type(value[0]) == int and type(value[1] == int):
                self.__position = value
            else:
                raise TypeError(
                        "position must be atuple of 2 positive integers")

    def area(self):
        """
        Evaluates the Area of the square
        Args:
            None
        Returns:
            result of area calculated (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square with '#' with positioning
        Args:
            None
        Return:
            None
        """
        a = self.__size
        p = self.__position
        if a == 0:
            print()
        p_x = " " * p[0]
        p_y = "\n" * p[1]
        print(p_y, end='')
        for _ in range(a):
            print(p_x, end='')
            for _ in range(a):
                print("#", end='')
            print()
