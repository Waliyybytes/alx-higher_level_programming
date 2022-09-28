#!/usr/bin/python3
"""
    JSON load from a file
"""
import json


def load_from_json_file(filename):
    """function to load from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        my_obj = json.load(f)
        return my_obj
