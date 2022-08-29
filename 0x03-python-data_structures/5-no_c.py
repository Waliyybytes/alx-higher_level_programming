#!/usr/bin/python3
def no_c(my_string):
    new = []
    for s in my_string:
        if s != "c":
            new.append(s)
    return ''.join(new)
