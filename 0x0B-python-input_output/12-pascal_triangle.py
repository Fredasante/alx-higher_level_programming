#!/usr/bin/python3
"""Module 12-pascal_triangle
returns a list of lists of integers representing
the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        -n: size of the triangle
    Returns:
        -a list of list of integers
    """
    if n <= 0:
        return []
    matrix = [[1]]
    for i in range(1, n):
        temp = [0] + matrix[-1] + [0]
        lil_matrix = []
        for j in range(len(matrix[-1]) + 1):
            lil_matrix.append(temp[j] + temp[j + 1])
        matrix.append(lil_matrix)
    return matrix
