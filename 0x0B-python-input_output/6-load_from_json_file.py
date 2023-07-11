#!/usr/bin/python3
"""
This module creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """opening file and deserializing contents"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
