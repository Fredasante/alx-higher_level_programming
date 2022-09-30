#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for idx in range(1, len(roman_string)):
        num = roman.get(roman_string[idx])
        prev_num = roman.get(roman_string[idx - 1])

        if num > prev_num:
            number += num - prev_num * 2
        else:
            number += num
    number += roman.get(roman_string[0])
    return number
