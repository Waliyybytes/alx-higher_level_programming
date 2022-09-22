#!/usr/bin/python3
"""
    Function to insert indentation in a text 

    Positions are after sighting '.' or '?' or ':'
"""


def text_indentation(text):
    """
        Function definition on insert indentation 
        and prints every line before any of the search characters

        Args:
            text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    tok = ""
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            tok += '\n\n'
            if text[i + 1] == " ":
            	i += 1
        else:
            tok += text[i]
        i += 1
    print(tok, end='')
