#!/usr/bin/python3
"""
Creates a class base
"""
class Base:
    """
    parent class

    Attributes:
        __nb_objects {int}: tracks number of instances
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        initialises object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
