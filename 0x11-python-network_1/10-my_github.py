#!/usr/bin/python3
""" my Github id """
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    checks = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=checks)
    j_obj = r.json()
    print(j_obj.get('id'))
