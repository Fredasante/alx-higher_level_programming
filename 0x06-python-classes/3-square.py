#!/usr/bin/python3
"""A class Square that defines a square."""


class Square:
    """Represents a square.
    Private instance attribute: size
    Instantiation with optional size.
    Public instance method: def area(self).
    """
    def __init__(self, size=0):
        """Initializes the object's data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns a square's area."""
        sq_area = self.__size ** 2
        return sq_area
