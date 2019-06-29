#!/usr/bin/python3
"""File for converting into json and from json"""
import json


class FileStorage:
    """Class for FileStorage to do json convertion"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        __objects[obj.__class__.__name__ + "." + obj.id] = {str(
            self.__class__.__name__) + str(self.id + self.__dict__)}

    def save(self):
        """A function that serializes __objects to the JSON file"""
        with open(__file_path, "w") as f:
            f.write(json.dumps(__objects))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        with open(self.__file_path, "r") as f:
            return (json.load(f))
