#!/usr/bin/python3
"""
    State class file for object creation
    and manipulation in HBnB console.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        State class implementation

        Attributes:
        name - string representing the name of the state
    """
    name = ""
