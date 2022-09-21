#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char is not ord('e') and char is not ord('q'):
        print("{:c}".format(char), end="")
