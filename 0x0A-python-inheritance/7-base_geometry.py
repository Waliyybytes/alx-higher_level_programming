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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
