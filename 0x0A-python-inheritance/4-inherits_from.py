#!/usr/bin/python3
"""
Checks for inheritance
"""


def inherits_from(obj, a_class):
    """Check if obj's class is a child of class"""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
