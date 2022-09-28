#!/usr/bin/python3
"""
    Reading files 
"""


def read_file(filename=""):
    """ method definitiion to read a file"""
    with open(filename) as f:
        print(f.read())
