#!/usr/bin/python3
"""Module 2-append_write
Appends text to a file.
"""


def append_write(filename="", text=""):
    """Appends  string to the end of a file.
    Args:
        -filename: name of file
        -text: text to append to end of file
    Returns:
        number of characters appended to file.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        num_chars = f.write(text)
    return num_chars
