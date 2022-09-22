#!/usr/bin/python3
"""
    Contains function to test

    Function:
        add_integer

"""


def add_integer(a, b=98):
    """ A function that returns addition of two numbers
         Making sure a and b are integers

        Arguments:
            a, b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
