#!/usr/bin/python3
def rev_alpha():
    for j in range(122, 96, -1):
        if j % 2 == 1:
            j -= 32
        print("{}".format(chr(j)), end='')
