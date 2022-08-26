#!/usr/bin/python3
import sys


def command_line():
    argv = sys.argv
    if len(argv) == 1:
        print(f"{len(argv) - 1} arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
        print(f"{len(argv) - 1}: {argv[1]}")
    else:
        print(f"{len(argv) - 1} arguments:")
        for i in range(len(argv) - 1):
            print(f"{i + 1}: {argv[i + 1]}")


if __name__ == "__main__":
    command_line()
