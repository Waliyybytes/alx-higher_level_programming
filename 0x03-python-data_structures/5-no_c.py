#!/usr/bin/python3
def no_c(my_string):
    new = []
    for s in my_string:
        if s is not "c":
            new.append(s)
    return ''.join(new)
