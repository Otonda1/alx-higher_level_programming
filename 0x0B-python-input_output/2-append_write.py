#!/usr/bin/python3
"""
this module appends a string at the end
of atext file
"""

def append_write(filename="", text=""):
    """
    returns the number of chararcters added
    """
    with open(filename, mode = 'a', encoding = 'utf-8') as f:
        return f.write(text)
