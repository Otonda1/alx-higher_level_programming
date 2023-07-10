#!/usr/bin/python3
"""
Checks if object is instance of specified class
"""


def is_same_class(obj, a_class):
    """Checks if object is instance of a class"""

    if type(obj) == a_class:
        return True
    return False
