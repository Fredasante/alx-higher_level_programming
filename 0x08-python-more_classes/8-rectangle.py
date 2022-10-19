#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """Represents a rectangle.
    Attributes:
        number_of_instances: number of rectangle instances
        increments with every instantiation and decrements
        with every deletion.
        print_symbol: Used as symbol for string representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the instances of the Rectangle.
        Args:
            width: rectangle's width
            height: rectangle's height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal string representation
        of an instance of a triangle filled with the
        '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ''
        for i in range(self.__height):
            for j in range(self. __width):
                string += str(self.print_symbol)
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """Returns a string representation of a Rectangle
        instance that can recreate a new instance by using
        eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a value.
        Args:
            value: value of width, must bea positive integer.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a value.
        Args:
            value: value of height, must be a positive integer.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle.
        Returns:
            Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle.
        Returns:
            Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the rectangle with the biggest area.
        Args:
            rect_1: first rectangle instance
            rect_2: second rectngle instance
        Returns:
            The instance with the biggest area or rect_1
            if they have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
