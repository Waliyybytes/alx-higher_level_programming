#!/usr/bin/python3
"""
    POST email to url
"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    data = parse.urlencode({'email': argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
