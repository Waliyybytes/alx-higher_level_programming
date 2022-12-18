#!/usr/bin/python3
""" fetches with package requests """
import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print(r.headers['X-Request-id'])
