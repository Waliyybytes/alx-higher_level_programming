#!/usr/bin/python3
"""
    Search and update a file
"""


def append_after(filename="", search_string="", new_string=""):
    """ functions to search and update"""
    with open(filename, 'r', encoding="utf-8") as f:
        fcopy = f.readlines()
        ls = len(fcopy)
        for i in range(ls):
            if search_string in fcopy[i]:
                fcopy = fcopy[:i+1] + [new_string] + fcopy[i+1:]
                i += 1
    with open(filename, 'w', encoding="utf-8") as f:
        f.write("{}".format("".join(fcopy)))
