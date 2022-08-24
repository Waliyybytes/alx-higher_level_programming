#!/usr/bin/python3
def fizzbuzz():
    for j in range(1, 101):
        if j % 3 == 0 and j % 5 != 0:
            print("Fizz", end=" ")
        elif j % 5 == 0 and j % 3 != 0:
            print("Buzz", end=" ")
        elif j % 15 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{}".format(j), end=" ")
