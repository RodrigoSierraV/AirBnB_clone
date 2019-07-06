#!/usr/bin/python3
"""Module to host the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that describes user's attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
