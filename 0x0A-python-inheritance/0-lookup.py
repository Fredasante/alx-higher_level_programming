#!/usr/bin/python3
"""Module 0-lookup
 returns the list of available attributes and methods
of an object.
"""


def lookup(obj):
    """Returns a list object of available attributes
    and methods of an object.
    Args:
        obj: object to lookup
    Returns:
        A list of attributes and methods of the object.
    """
    return dir(obj)
