#!/usr/bin/python3
import os

def easy_print():
    st = "#pythoniscool\n"
    line = str.encode(st)
    os.write(1, line)


if __name__ == "__main__":
    easy_print()
