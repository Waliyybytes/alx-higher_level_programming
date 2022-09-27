#!/usr/bin/python3
"""
    To demonstrate Inheritance

"""


class MyList(list):
    """ 
        Class to demonstrate inheritance 
        Inherits from class list

    """
    def print_sorted(self):
        """ 
            method to demonstrate inheritance

        """
        print(sorted(self))
