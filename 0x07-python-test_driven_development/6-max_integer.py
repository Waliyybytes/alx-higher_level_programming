#!/usr/bin/python3
"""
    Function to find maximum number in a list

"""


def max_integer(list=[]):
    """
        Function definition with checks of type
        
        Args:
            list (given)
    """
    if len(list) == 0:
        return None
    mags = list[0]
    i = 1
    while i < len(list):
        if list[i] > mags:
            mags = list[i]
        i += 1
    return mags
