#!/usr/bin/python3
def no_c(my_string):
    new = []
    if not my_string:
        return
    for s in my_string:
        if s != 'c':
            new.append(s)
    return ''.join(new)
