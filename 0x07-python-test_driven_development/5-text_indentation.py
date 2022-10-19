#!/usr/bin/python3
"""Module text_indentation
Prints a text with 2 new lines after the characters:
'.', '?' and ':'
"""


def text_indentation(text):
    """Indents text after the characters: '.', '?', ':'."""
    if type(text) is not str:
        raise TypeError('text must be a string')
    char_list = ['.', '?', ':']
    line = ""
    for word in text:
        if word not in char_list:
            line += word
        else:
            line += word
            print(line.strip() + '\n')
            line = ""
    print(line.strip(), end="")
