#!/usr/bin/python3
"""
    Appending text to files
"""


def append_write(filename="", text=""):
    """ method definitiion to append write to a file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
