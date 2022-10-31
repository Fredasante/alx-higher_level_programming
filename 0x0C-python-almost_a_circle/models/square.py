#!/usr/bin/python3
"""Module Square
Contains the class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square.
    Private instance attribute: size
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: x
        - property def x(self)
        - property setter def x(self, value)
    Private instance attribute: y
        - property def y(self)
        - property setter def y(self, value)
    Class constructor: def __init__(self, size, x=0, y=0, id=None)
    Public instance method: def area(self)
    Public instance method: def display(self)
    Public instance method: def update(self, *args)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialises our Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the width"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the width and height through their setters."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """Prints an informal string representation of an object."""
        return "[{}] ({}) {}/{} - {}".format(
                                            self.__class__.__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width
                                            )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.
        Args:
            - *args: positional arguments
            - **kwargs: keyworded arguments
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square."""
        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict
