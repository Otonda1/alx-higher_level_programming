#!/usr/bin/python3
"""
Module that creates Pascal's triangle of integers
"""


def pascal_triangle(n):
    """Create a Pascal's triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
