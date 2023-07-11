#!/usr/bin/python3
"""
This module defines a function that reads a textfile\
        and prints it out to the std output
"""
def read_file(filename=""):
    """
    This function reads a file and prints it out to the std out
    """
    with open(filename, encoding = 'utf-8') as f:
        fread = f.read()
        print(fread)
