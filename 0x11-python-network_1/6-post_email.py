#!/usr/bin/python3
"""
    post email to url
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    args = {'email': argv[2]}
    r = requests.post(url, data=args)
    print(r.text)
