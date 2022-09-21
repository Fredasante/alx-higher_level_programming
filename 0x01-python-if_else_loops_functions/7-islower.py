#!/usr/bin/python3
def islower(c):
    for char in range(ord('a'), ord('z') + 1):
        if ord(c) == char:
            return True
    return False
