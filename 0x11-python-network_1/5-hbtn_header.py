#!/usr/bin/python3
""" fetches with package requests """
import requests
from sys import argv


r = requests.get(argv[1])
print(r.headers['X-Request-id'])
