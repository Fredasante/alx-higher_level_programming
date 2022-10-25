#!/usr/bin/python3
"""Module 8-rectangle
class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry
    Instantiation with width and height
    Private instance attributes: width, height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
