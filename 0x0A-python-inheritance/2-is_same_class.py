#!/usr/bin/python3
"""Module 2-is_same_class
Checks if an object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the
    specified class.
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if it is an instance of the class and false otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
