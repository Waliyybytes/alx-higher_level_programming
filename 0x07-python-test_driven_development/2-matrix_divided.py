#!/usr/bin/python3
"""
    This is a matrix division module

    Contains a function:
        matrix_divided

"""


def matrix_divided(matrix, div):
    """
    Matrix definition

    Args:
        matrix(a given matrix)
        div(a divisor)
    """
    for mat in matrix:
        lt = len(matrix[0])
        if len(mat) != lt:
            raise TypeError("Each row of the matrix must have the same size")
        for i in mat:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivsionError("division by zero")
    return [[round(num / div, 2) for num in mat] for mat in d_matrix]
