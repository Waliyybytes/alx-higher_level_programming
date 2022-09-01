#!/usr/bin/python3
def uniq_add(my_list=[]):
    for num in sorted(my_list):
        if my_list.count(num) > 1:
            my_list.remove(num)
        else:
            total += num
    return total
