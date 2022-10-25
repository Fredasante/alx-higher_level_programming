#!/usr/bin/python3
"""Module 10-student
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
    Public method def reload_from_json(self, json)
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a Student instance.
        Args:
            -attrs: list of attributes
        Returns:
            -a dictionary representation of a Student instance
        """
        my_dict = dict()
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            for attr in attrs:
                if attr in self.__dict__:
                    my_dict.update({attr: self.__dict__[attr]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance.
        Args:
            -json: dictionary
        """
        for key, val in json.items():
            self.__setattr__(key, val)
