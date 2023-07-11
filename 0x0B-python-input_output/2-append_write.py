#!/usr/bin/python3
"""
This module appends a string at the end
of a text file
"""


def append_write(filename="", text=""):
    """opening the file for writing"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
