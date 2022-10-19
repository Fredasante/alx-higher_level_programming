#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices.
    and returns a new matrix.
    """
    matrix = np.matmul(m_a, m_b)
    return matrix
