#!/usr/bin/python3
import hidden_4


def unravel():
    for name in hidden_4:
        if name[0] != '_':
            print(name)


if __name__ == "__main__":
    unravel()
