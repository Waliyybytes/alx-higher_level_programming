#!/usr/bin/python3
"""
    Base Geometry module creation

"""


class BaseGeometry():
    """
        Creattion of class BaseGeometry

    """
    def area(self):
        """
            Method to implement area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            To validate the attribute 'value'

        """
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
