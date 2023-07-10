#!/usr/bin/python3
"""
Module containing class BaseGeometry
"""


class BaseGeometry:
    """Defining the class attributes"""
    pass

    def area(self):
        """Undefined method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if parameter is integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Child of BaseGeometry, defines a rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
