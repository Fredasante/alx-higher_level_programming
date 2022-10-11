#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    """
    def __init__(self, size=0):
        """Initializes the object data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
