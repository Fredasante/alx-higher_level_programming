#!/usr/bin/python3
"""Module 100-append_after
inserts a line of text to a file, after each
line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """appends a new string after a specified string
    Args:
        -filename: name of file
        -search_string: string to append after
        -new_string: new string to append to file
    """
    my_str = ""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            my_str += line
            if search_string in line:
                my_str += new_string

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(my_str)
