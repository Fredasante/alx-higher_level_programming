#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    last_num = number % 10
    print(last_num, end="")
    return last_num
