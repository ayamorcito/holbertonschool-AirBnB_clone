#!/usr/bin/python3
"""
    Review class file for object creation
    and manipulation in HBnB console.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class implementation

        Attributes:
        text - string containing the review text
        place_id - string containing the unique place_id
        user_id - string containing the unique user_id
    """
    text = ""
    place_id = ""  # empty string but it will be Place.id
    user_id = ""  # empty string but it will be User.id
