#!/usr/bin/python3
"""
   fetches URL https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        result = response.read()
        print('Body response:')
        print(f"\t- type: {type(result)}")
        print(f"\t- content: {result}")
        print('\t- utf8 content: {}'.format(result.decode('utf-8')))
