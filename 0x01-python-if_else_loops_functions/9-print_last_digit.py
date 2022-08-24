#!/usr/bin/python3
def print_last_digit(number):
    new = abs(number) % 10
    print("{}".format(new), end='')
    return new
