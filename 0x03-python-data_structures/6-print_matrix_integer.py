#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    separator = ' '
    for i in matrix:
        print(separator.join("{:d}".format(j) for j in i))
