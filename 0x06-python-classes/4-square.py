#!/usr/bin/python3
"""Defining a class named Square with size validation"""


class Square:
    """
    Instantiation of Square's objects and attributes
    args:
        size - should be an integer greater than 0
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
