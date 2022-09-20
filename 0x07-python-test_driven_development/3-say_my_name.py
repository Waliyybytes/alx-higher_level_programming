#!/usr/bin/python3
"""
    Contains a function tell us your name

    my name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        Function definition and putting in place all checks

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("first_name must be a string")
    message = f"My name is {first_name.title()} {last_name.title()}"
    print(message)
