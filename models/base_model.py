#!/usr/bin/python3
"""File for BaseModel"""
import uuid
import datetime
import time
import models


class BaseModel:
    """Class for BaseModel"""

    def __init__(self, *args, **kwargs):
        """It initializes the variables using args and kwargs"""

        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'created_at' in kwargs:
            self.created_at = datetime.datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Function that allows to print the info of the model"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Function that updates new information"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Function returns a dictionary containing all keys/values"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
