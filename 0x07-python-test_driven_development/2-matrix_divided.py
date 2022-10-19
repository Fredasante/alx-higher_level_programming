#!/usr/bin/python3
"""Module matrix_divided
Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides a matrix by a divisor
    Returns a new matrix.
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    if len(matrix) == 0 or not isinstance(matrix, list) or not matrix[0]:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')
    for row in matrix:
        if isinstance(row, list):
            row_len = len(row)
            break
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists)' +
                            ' of integers/floats')
        if len(row) != row_len:
            raise TypeError('Each row of the matrix must have the same size')
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')
            new_row.append(round(col / div, 2))
        new_matrix.append(new_row)
    return new_matrix
