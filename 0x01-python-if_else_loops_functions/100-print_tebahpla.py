#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 != 0:
        char -= 32
    print("{:c}".format(char), end="")
