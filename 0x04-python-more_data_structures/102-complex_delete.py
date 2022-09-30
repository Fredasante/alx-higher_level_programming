#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = []
    for key, val in a_dictionary.items():
        if val == value:
            key_list.append(key)
    for item in key_list:
        del a_dictionary[item]
    return a_dictionary
