#!/usr/bin/python3
import sys


def command_line():
    add = 0
    for i in sys.argv[1:]:
        add += int(i)
    print(add)


if __name__ == "__main__":
    command_line()
