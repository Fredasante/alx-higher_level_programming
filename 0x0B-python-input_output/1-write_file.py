#!/usr/bin/python3
"""Module 1-write_file.
Writes to a textfile.
"""


def write_file(filename="", text=""):
    """Writes text to a text file.
    Args:
        -filename: name of file
        -text: data to insert into file.
    Returns:
        number of characters written into file
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
