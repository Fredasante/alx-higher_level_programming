#!/usr/bin/python3
"""Module 5-save_to_json_file
writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes a serialized object to a text file.
    Args:
        -my_obj: python object to write to file
        -filename: name of file to write into.
    """
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
