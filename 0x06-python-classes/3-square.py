#!/usr/bin/python3
"""Defining a class named Square with size validation"""


class Square:
    """
    Instantiation of Square's objects and attributes
    args:
        size - should be an integer greater than 0
    """
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
