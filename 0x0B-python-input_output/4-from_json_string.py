#!/usr/bin/python3
"""
Module that converts JSON string to python
data object
"""
import json


def from_json_string(my_str):
    """deserializing JSON string"""
    return json.loads(my_str)
