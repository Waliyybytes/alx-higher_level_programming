#!/usr/bin/python3
"""
    writing files
"""


def write_file(filename="", text=""):
    """ method definitiion to write to a file"""
    with open(filename, mode = 'w', encoding="utf-8") as f:
        return f.write(text)
