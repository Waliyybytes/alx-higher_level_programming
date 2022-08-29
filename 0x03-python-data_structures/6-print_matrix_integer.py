#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for rows in matrix:
        for i in rows:
            if rows.index(i) != len(rows) - 1:
                print("{:d}".format(i), end=' ')
            else:
                print("{:d}".format(i))
