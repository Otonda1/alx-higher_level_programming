#!/usr/bin/python3
"""
This Module converts object to its JSON
representation, and saves it in a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves my_obj's JSON representation in file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
