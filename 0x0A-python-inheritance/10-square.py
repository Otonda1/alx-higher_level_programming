#!/usr/bin/python3
"""
This module defines a Square subclass of Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines Square attributes"""

    def __init__(self, size):
        """Instantiates a new square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
