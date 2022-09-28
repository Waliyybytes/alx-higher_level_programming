#!/usr/bin/python3
"""
    JSON module

"""
import json


def from_json_string(my_str):
    """ converting json format to string format"""
    my_obj = json.loads(my_str)
    return my_obj
