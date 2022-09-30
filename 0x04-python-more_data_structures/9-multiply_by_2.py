#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = a_dictionary.get(key) * 2
    return new_dict
