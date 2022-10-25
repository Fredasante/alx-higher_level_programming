#!/usr/bin/python3
"""Module 9-student
Defining a student.
"""


class Student:
    """Defines a student.
    Public instance attributes:
        -first_name
        -last_name
        -age
    Instantiation with first_name, last_name and age.
    Public method def to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of
        a Student instance.
        """
        return self.__dict__
