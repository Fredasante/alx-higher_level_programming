#!/usr/bin/python3

def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
        print("Inside result: {}".format(res))
    except ZeroDivisionError:
        res = None
        print("Inside result: {}".format(res))
    finally:
        return res
