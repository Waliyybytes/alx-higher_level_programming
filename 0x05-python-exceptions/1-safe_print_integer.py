#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        bul = True
    except ValueError:
        bul = False
    return bul
