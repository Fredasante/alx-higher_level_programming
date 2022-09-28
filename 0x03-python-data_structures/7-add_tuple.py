#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    tup_a = tuple_a + (0, 0)
    tup_b = tuple_b + (0, 0)
    tuple_c = tup_a[0] + tup_b[0], tup_a[1] + tup_b[1]
    return tuple_c
