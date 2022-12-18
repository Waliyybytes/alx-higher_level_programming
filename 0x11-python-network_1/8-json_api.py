#!/usr/bin/python3
""" Search API with letter """
import requests
from sys import argv


def search() -> None:
    """ post on url and search api wih letter"""
    char = "" if len(argv) < 2 else argv[1]
    dat = {'q' : char}
    r = requests.post("http://0.0.0.0:5000/search_user", data=dat)

    try:
        u = r.json()
    except Exception:
        print('Not a valid JSON')
    else:
        if len(u):
            print('[{}] {}'.format(u['id'], u['name']))
        else:
            print('No result')
