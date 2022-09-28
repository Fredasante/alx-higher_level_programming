#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        first_char = None
    else:
        first_char = sentence[:1]
    tup_c = (str_len, first_char)
    return tup_c
