#!/usr/bin/python3
"""
Module that writes a string into a file
"""


def write_file(filename="", text=""):
    """Writes into a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
