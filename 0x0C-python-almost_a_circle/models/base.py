#!/usr/bin/python3
"""Module base
Includes the projects base class Base.
"""


import json


class Base:
    """base class of our project.
    Public instance attribute: id
    Private class attribute: __nb_objects = 0
    Class constructor: def __init__(self, id=None)
    Static method: def to_json_string(list_dictionaries)
    Class method: def save_to_file(cls, list_objs)
    Static method: def from_json_string(json_string)
    Class method: def create(cls, **dictionary)
    Class method: def load_from_file(cls)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes our class instance.
        Args:
            - id: argument value of type int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.
        Args:
            - list_dictionaries: list of dictionaries.
        Returns:
            - json string representation of the list object
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.
        Args:
            - list_objs: list of class instances.
        """
        file_name = "{}.json".format(cls.__name__)
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w", encoding="utf-8") as fd:
            json.dump(content, fd)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.
        Args:
            - json_string: json string representation of a list object
        Returns:
            - list object
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.
        Args:
            - dictionary: keyworded arguments of instance attributes
        Returns:
            - class instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """retrieves a list of instances from a json file.
        Returns:
            - list of class instances
        """
        file_name = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(file_name, encoding="utf-8") as f:
                data = f.read()
                objs = cls.from_json_string(data)
                for o in objs:
                    instances.append(cls.create(**o))
        except FileNotFoundError:
            pass
        return instances
