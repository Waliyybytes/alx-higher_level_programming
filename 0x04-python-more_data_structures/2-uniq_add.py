#!/usr/bin/python3
def uniq_add(my_list=[]):
    for num in sorted(matrix):
        if matrix.count(num) > 1:
            matrix.remove(num)
        else:
            total += num
    return total
