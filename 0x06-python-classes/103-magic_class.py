#!/usr/bin/python3
"""
This module is to evaluate the Area and Circumference of a Circle

"""

import math
import dis


class MagicClass:
    """ Class Definition
        Methods:
            area, circumference
        Attributes:
            Radius
    """
    def __init__(self, radius):
        """Initialises a class"""
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """ Evaluates and returns the Area of a circle """
        return (self.radius ** 2) * math.pi

    def circumference(self):
        """ Evalautes and returns the Circumference of a circle"""
        return 2 * math.pi * self.radius
