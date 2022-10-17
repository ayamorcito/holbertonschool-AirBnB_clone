#!/usr/bin/python3
"""
    Amenity class file for object creation
    and manipulation in HBnB console.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity class implementation

        Attributes:
        name - string representing the name of the amenity
    """
    name = ""
