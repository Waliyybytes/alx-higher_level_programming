#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        val = max(a_dictionary.values())
        key_idx = list(a_dictionary.values()).index(val)
        return list(a_dictionary.keys())[key_idx]
