#!/usr/bin/python3
"""
    Function to find maximum in a list

"""

def max_integer(list=[]):
    """
        Function definition with checks of type
        
        Args:
            list (given)
    """
    for item in list:
        if type(item) not in [int, float]:
            raise TypeError("list must contain only integer/floats")
    return max(list)
