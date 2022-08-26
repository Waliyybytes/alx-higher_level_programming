#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


import sys
def my_calculator():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        a = int(argv[1])
        b = int(argv[3])
        match argv[2]:
            case '+':
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            case '-':
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            case '*':
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            case '/':
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")


if __name__ == "__main__":
    my_calculator()
