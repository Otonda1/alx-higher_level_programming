#!/usr/bin/python3
"""
Creating a child of the list class
"""


class MyList(list):
    """Inherits from inbuilt list class"""

    def print_sorted(self):
        """Returns a sorted list"""
        print(sorted(self))
    
