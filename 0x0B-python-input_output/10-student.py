#!/usr/bin/python3
"""
Defines class Student and retrieves dictionary representation
of a Student instance
"""


class Student:
    """Defining the class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a student instance"""
        if isinstance(attrs, list) and all([type(i) == str for i in attrs]):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
