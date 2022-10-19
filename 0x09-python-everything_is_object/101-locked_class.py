#!/usr/bin/python3
"""Locked Class with no class or object attribute."""


class LockedClass:
    """prevents the user from dynamically creating new
    instance attributes, except if the new instance
    attribute is called first_name.
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """Initializes the object's instance."""
        self.first_name = first_name
