#!/usr/bin/python3
"""
    Implements Pascals Triangle
"""


def pascal_triangle(n):
    """ function implementation """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(0, n):
        if i == 0:
            pascal.append([1])
        if i > 0:
            get = [1]
            for j in range(1, i):
                get.append(pascal[i-1][j] + pascal[i-1][j-1])
            get.append(1)
            pascal.append(get)
    return pascal
