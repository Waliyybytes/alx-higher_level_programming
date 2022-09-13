#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        bul = True
    except (ValueError, TypeError) as err:
        print(f"Exception: {err}", file=sys.stderr)
        bul = False
    return bul
