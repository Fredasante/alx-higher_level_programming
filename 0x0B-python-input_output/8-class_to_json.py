#!/usr/bin/python3
"""Module 8-class_to_json
Returns class instance attributes for serialization
"""


def class_to_json(obj):
    """Converts a python class instance to a
    dictionary description.
    Args:
        -obj: python class instance
    Returns:
        -class instance attributes
    """
    return obj.__dict__
