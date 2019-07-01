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
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """A function that serializes __objects to the JSON file"""
        tojson = {}
        for key in self.__objects:
            tojson[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(tojson, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)

            for key, value in data.items():
                self.__objects[key] = BaseModel(value)
            return self.__objects
        except:
            pass
