#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list."""


class Node:
    """Represents a node of a singly linked list.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def data(self, value)
    Instantiation with data and next_node.
    """
    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the node's data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the node's data to a value."""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the address of the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the address of the next node to a value."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


"""A class SinglyLinkedList that defines a singly linked list."""


class SinglyLinkedList:
    """Represents a singly linked list.
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """
    def __init__(self):
        """Initialiazes the data of the linked list."""
        self.__head = None

    def __str__(self):
        """To print the node's data."""
        data_str = ""
        current = self.__head
        while current:
            data_str += str(current.data)
            data_str += '\n'
            current = current.next_node
        return data_str[:-1]

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
        in the list (increasing order).
        """
        new_node = Node(value)
        current = self.__head
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while current.next_node:
                if current.next_node.data > value:
                    new_node.next_node = current.next_node
                    break
                else:
                    current = current.next_node
            current.next_node = new_node
