#!/usr/bin/python3
def fizzbuzz():
    for j in range(1, 100):
        if j % 3 == 0 and j % 5 != 0:
            print("fizz", end=" ")
        elif j % 5 == 0 and j % 3 != 0:
            print("buzz", end=" ")
        elif j % 15 == 0:
            print("fizzbuzz", end=" ")
        else:
            print("{}".format(j), end=" ")
