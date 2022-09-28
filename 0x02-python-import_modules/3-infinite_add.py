#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    res = 0
    if num_args == 0:
        print("0")
    else:
        for idx in range(1, num_args + 1):
            res += int(sys.argv[idx])
        print(res)
