#!/usr/bin/python3
"""File for converting into json and from json"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Class for FileStorage to do json convertion"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """A function that serializes __objects to the JSON file"""
        with open(self.__file_path, "a") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                return (json.load(f))
        except:
            pass
