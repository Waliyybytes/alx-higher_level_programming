#!/usr/bin/python3
"""
    JSON module

"""
import json


def to_json_string(my_obj):
    """ converting to json format"""
    to_json = json.dumps(my_obj, ensure_ascii=False, sort_keys=True)
    return to_json
