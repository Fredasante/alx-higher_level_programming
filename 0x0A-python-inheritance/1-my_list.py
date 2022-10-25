#!/usr/bin/python3
"""Module 1-my_list
Contains a class MyList that inherits from list.
"""


class MyList(list):
    """It inherits from list.
    Public instance method: def print_sorted(self)
    """
    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
