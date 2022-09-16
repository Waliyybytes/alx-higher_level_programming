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
            if len(value) != 2 or type(value[0]) is not int \
                        or type(value[1]) is not int \
                        or value[0] < 0 or value[1] < 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers")
            else:
                self.__position = value

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
            return
        p_x = " " * p[0]
        for _ in range(p[1]):
            print()
        for _ in range(a):
            print(p_x, end='')
            for _ in range(a):
                print("#", end='')
            print()

    def __str__(self):
        """
        Prints a square instance
        A string representation of the   square
        """
        rep = ""
        a = self.__size
        p = self.__position
        if a == 0:
            return ''
        p_x = " " * p[0]
        p_y = "\n" * p[1]
        sqr = "#" * a
        rep += p_y
        for i in range(a):
            rep += p_x
            rep += sqr
            if i != a - 1:
                rep += '\n'
        return rep
