#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    main_list = []
    for row in matrix:
        new = list(map(lambda x: x ** 2, row))
        main_list.append(new)
    return main_list
