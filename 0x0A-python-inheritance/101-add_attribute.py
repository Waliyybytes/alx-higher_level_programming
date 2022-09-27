#!/usr/bin/python3
"""
    module tesing objects to add attributes
"""


def add_attribute(obj, name, value):
    """ method definition to check attribute addition"""
    if '__dict__' in dir(obj) and isinstance(type(obj), object):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
