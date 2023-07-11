#!/usr/bin/python3
"""
Module that prints a file's contents to
stdout
"""


def read_file(filename=""):
    """Open the file and read from it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
