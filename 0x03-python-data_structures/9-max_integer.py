#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > biggest:
            biggest = num
    return biggest
