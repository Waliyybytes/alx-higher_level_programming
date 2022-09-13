#!/usr/bin/python3
def safe_print_division(x, y):
    print("Inside result: ", end='')
    try:
        result = x / y
    except ZeroDivisionError:
        result = None
    finally:
        print("{}".format(result))
    return result
