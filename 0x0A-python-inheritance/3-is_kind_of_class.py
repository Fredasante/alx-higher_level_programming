#!/usr/bin/python3
"""Module 3-is_kind_of_class
Checks if an object is an instance of, or if the object is
an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is instance of a class or instance of
    a subclass of that class.
    Args:
        obj: object to check
        a_class: class to compare object to.
    Returns:
        True if it is an instance of the class or a subclass
        of the class.
    """
    if isinstance(obj, a_class):
        return True
    return False
