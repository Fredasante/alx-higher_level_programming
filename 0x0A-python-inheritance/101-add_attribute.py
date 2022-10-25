#!/usr/bin/python3
"""Module 101-add_attribute
Adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, attr, value):
    """Checks if an attribute can be added to an object.
    Args:
       obj: object to add attribute to
       attr: attribute name
       value: value of attribute
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, attr):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
