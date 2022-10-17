#!/usr/bin/python3
"""
    City class file for object creation
    and manipulation in HBnB console.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        City class implemetation

        Attributes:
        name - string representing the name of the city
        state_id - string representing the state_id
    """
    name = ""
    state_id = ""  # empty. it will be the State.id
