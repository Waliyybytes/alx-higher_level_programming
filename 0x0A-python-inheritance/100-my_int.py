#!/usr/bin/python3
"""
    MyInt module
"""


class MyInt(int):
    """ definition of class MyInt"""
    def __eq__(self, other):
        """ reverts equals """
        return False

    def __ne__(self, other):
        """ reverts 'not equals'"""
        return True
