#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """
    def __init__(self, size):
        """Initializes the object data."""
        self.__size = size
