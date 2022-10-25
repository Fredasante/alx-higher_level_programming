#!/usr/bin/python3
"""Module 10-square.py
 a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square.
    Instantiation with size: def __init__(self, size)
    Private instnace attributes: size
    Public instance method def area()
    """

    def __init__(self, size):
        """Initializes an object.
        Args:
            size: value to initialise object with.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Finds the area of a square."""
        return self.__size ** 2

    def __str__(self):
        """Prints an informal string representation
        of an object.
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
