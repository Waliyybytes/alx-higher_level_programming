#!/usr/bin/python3
"""
    Module to lock a class with only one attribute
"""


class LockedClass:
    """
        To dynamically prevent creation of other instance attributes

        Except first_name
    """

    __slots__ = ['first_name']
