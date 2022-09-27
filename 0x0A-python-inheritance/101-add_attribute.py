#!/usr/bin/python3
"""
    module tesing objects to add attributes
"""


def add_attribute(obj, name, value):
    """ method definition to check attribute addition"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
