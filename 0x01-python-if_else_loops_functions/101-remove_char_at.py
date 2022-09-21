#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for idx in range(len(str)):
        if idx != n:
            str_cpy += str[idx]
    return str_cpy
