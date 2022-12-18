#!/usr/bin/python3
""" fetches with package requests """
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers['X-Request-id'])
