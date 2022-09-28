#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ['+', '-', '*', '/']
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if op == '+':
            res = add(a, b)
        elif op == '-':
            res = sub(a, b)
        elif op == '*':
            res = mul(a, b)
        else:
            res = div(a, b)
        print("{} {} {} = {}".format(a, op, b, res))
