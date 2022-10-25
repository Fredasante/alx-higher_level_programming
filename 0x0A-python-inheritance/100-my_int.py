#!/usr/bin/python3
"""Module 100-my_int
inverts the __ne__ and __eq__ methods.
"""


class MyInt(int):
    """Class inheriting from int."""

    def __eq__(self, other):
        """Equality becomes inequality."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality."""
        return super().__eq__(other)
