#!/usr/bin/python3
from add_0 import add


def addition():
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))


if __name__ == "__main__":
    addition()
