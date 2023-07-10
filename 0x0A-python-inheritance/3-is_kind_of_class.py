#!/usr/bin/python3
"""
Checks if object is instance of current class or its parents
"""


def is_kind_of_class(obj, a_class):
    """Is obj an instance of a_class?"""

    if isinstance(obj, a_class):
        return True
    return False
