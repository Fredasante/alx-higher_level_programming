#!/usr/bin/python3
"""Module Rectangle
Contains the class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle.
    Private instance attribute: width
        - property def width(self)
        - property setter def width(self, value)
    Private instance attribute: height
        - property def height(self)
        - property setter def height(self, value)
    Private instance attribute: x
        - property def x(self)
        - property setter def x(self, value)
    Private instance attribute: y
        - property def y(self)
        - property setter def y(self, value)
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None)
    Public instance method: def area(self)
    Public instance method: def display(self)
    Public instance method: def update(self, *args)
    Public instance method: def to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises our Rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to the value"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to the value."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x to value."""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y to value."""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Calculates the area of our rectangle instance
        Returns:
            - the area value.
        """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        x = ' ' * self.x
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(x, end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """Prints an informal string representation of an object."""
        return "[{}] ({}) {}/{} - {}/{}".format(
                                                self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height
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
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        my_dict = {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
        return my_dict
