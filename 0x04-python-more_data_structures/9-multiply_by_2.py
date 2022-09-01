#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = {}
    for key, val in a_dictionary.items():
        b[key] = val * 2
    return b
