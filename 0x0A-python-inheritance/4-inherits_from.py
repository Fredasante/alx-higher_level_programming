#!/usr/bin/python3
"""Module 4-inherits_from
Checks if an object is an instance of a class that
inherited directly or indirectly from the specified
class.
"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class
    that inherited from the class.
    Args:
        obj: object to check
        a_class: class to cehck against
    Returns:
        True if object of an instance of a subclass
        to the class defined, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
