#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0:
        raise ValueError('m_b can\'t be empty')
    
