#!/usr/bin/python3
"""
    Load, add and save to a file
"""

if __name__ == "__main__":
    import json
    from sys import argv
    import os

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
            "6-load_from_json_file").load_from_json_file

    if os.path.exists('add_item.json'):
        with open('add_item.json') as f:
            items = json.load(f)
            items.extend(argv[1:])
    else:
        items = argv[1:]
    save_to_json_file(items, 'add_item.json')
    load_from_json_file('add_item.json')
