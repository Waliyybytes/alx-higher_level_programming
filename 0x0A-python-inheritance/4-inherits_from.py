#!/usr/bin/python3
"""
    To check the class inheritance

"""


def inherits_from(obj, a_class):
    """ checks  parents of obj"""
    return isinstance(obj, a_class) and type(obj) is not a_class
