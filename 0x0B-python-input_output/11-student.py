#!/usr/bin/python3
"""
    Class module to json
"""


class Student:
    """ Class definition with methods '__init__' and 'to_json'"""
    def __init__(self, first_name, last_name, age):
        """ class instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary description with
                simple data structure
            (list, dictionary, string, integer and boolean)
            for JSON serialization of an object
        """
        get_attrs = {}
        if attrs is not None:
            for key in self.__dict__:
                if key in attrs:
                    get_attrs[key] = self.__dict__[key]
            return get_attrs
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            if key in self.__dict__:
                setattr(self, key, json[key])
