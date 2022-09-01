#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_mul = 0
    sum_tup = 0
    for tup in my_list:
        sum_tup += tup[len(tup) - 1]
        mul = 0
        for i in range(1, len(tup)):
            mul += tup[i-1] * tup[-1]
        sum_mul += mul
    return sum_mul / sum_tup
