#!/usr/bin/python3
"""Module 7-base_geometry
Integer Validator.
"""


class BaseGeometry:
    """Basic class definition
    Public instance method: def area(self)
    Public instance method: def integer_validator(self, name, value)
    """

    def area(self):
        """Raises an exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value.
        Args:
            name: string
            value: integer(needs to be validated)
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
