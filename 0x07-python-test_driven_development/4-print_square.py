#!/usr/bin/python3
"""
    A module to print a sqaure with character '#'

    With additional checks and tests

"""


def print_square(size):
    """
        function definition with all checks in place

        Args:
            size (size of the square to print
    """
    import math

    if type(size) not in [int, float]:
        if math.trunc(size) != size:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float :
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
        exit()
    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print()
