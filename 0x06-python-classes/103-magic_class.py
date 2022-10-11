#!/usr/bin/python3
"""A MagicClass that does exactly the same as a Python bytecode."""
from math import pi


class MagicClass:
    """Represents a Circle.
    Private instance variable: radius
    Instantiation with a radius
    Public instance method: def area(self)
    Public instance method: def circumference(self).
    """
    def __init__(self, radius=0):
        """Instantiates a circle's radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of a circle."""
        return (self.__radius ** 2) * pi

    def circumference(self):
        """Returns the circumference of a circle."""
        return 2 * pi * self.__radius
