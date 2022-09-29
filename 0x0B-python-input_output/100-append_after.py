#!/usr/bin/python3
"""
    Search and update a file
"""


def append_after(filename="", search_string="", new_string=""):
    """method to search and update"""
    with open(filename, 'r', encoding="utf-8") as f:
        fcopy = []
        while True:
            line = f.readline()
            if line == "":
                break
            fcopy.append(line)
            if search_string in line:
                fcopy.append(new_string)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write("{}".format("".join(fcopy)))
