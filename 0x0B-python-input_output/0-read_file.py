#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """Reads a text file.
    Args:
        -filename: name of file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
