#!/usr/bin/python3
"""
    Module contains task to generate nqueens position on a
    n by n chessboard that are safe from each other.

    Checks on n was carried out

    Initialisation was done, then

    Recursive Backtracking was used

"""

from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if argv[1].isdigit() is False:
    print("N must be a number")
    exit(1)
if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(argv[1])
col = set()
posDg = set()
negDg = set()

res = []
for i in range(n):
    res.append([i, None])


def backtrack(r):
    """
        Backtracking function defined

    """

    if r == n:
        print(res)
    for c in range(n):
        # Checks if queen is present on column or diagonals
        if c in col or (r + c) in posDg or (r - c) in negDg:
            continue

        col.add(c)
        posDg.add(r + c)
        negDg.add(r - c)
        res[r][1] = c

        backtrack(r + 1)   # recursive calls by increasing row number

        # clears the sets for fresh starts
        col.remove(c)
        posDg.remove(r + c)
        negDg.remove(r - c)
        res[r][1] = None


if __name__ == "__main__":
    backtrack(0)
