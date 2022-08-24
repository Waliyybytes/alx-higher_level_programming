#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and i*10 + j < 10*j + i and i != 8:
            print('{}'.format(i) + '{}'.format(j), end=', ')
        if i == 8 and i*10 + j < 10*j + i:
            print('{}'.format(i) + '{}'.format(j))

