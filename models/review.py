#!/usr/bin/python3
from models.base_model import BaseModel
"""File for Review"""


class Review(BaseModel):
    """Class for Review, it creates the attributes"""

    place_id = ''
    user_id = ''
    text = ''
