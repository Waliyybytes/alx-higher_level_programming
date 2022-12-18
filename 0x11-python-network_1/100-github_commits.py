#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    query = {'page_limit': 10}
    r = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits', params=query)
    j_obj = r.json()

    for obj in j_obj:
        author = obj['commit']['author']
        print(f"{obj.get('sha')}:", author.get('name'))
