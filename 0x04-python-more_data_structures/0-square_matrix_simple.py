#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        square_matrix.append(list(map(lambda j: j ** 2, i)))
    return (square_matrix)
