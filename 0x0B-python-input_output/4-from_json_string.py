#!/usr/bin/python3
"""Module 4-from_json_string
Deserializes a json string.
"""


import json


def from_json_string(my_str):
    """Returns an object from a json string.
    Args:
        -my_str: json string to deserialize.
    Returns:
        -python object
    """
    return json.loads(my_str)
