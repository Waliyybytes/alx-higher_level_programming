#!/usr/bin/python3
"""
    JSON module

"""
import json


def save_to_json_file(my_obj, filename):
    """ converting to json format and saving in a file"""
    with open(filename, 'w', encoding="utf-8") as f :
        json.dump(my_obj, f, ensure_ascii=False, sort_keys=True)
