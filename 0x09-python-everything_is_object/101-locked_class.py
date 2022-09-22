#!/usr/bin/python3
class LockedClass:
    """
        To dynamically prevent creation of other instance attributes

        Except first_name
    """

    __slots__ = ['first_name']
