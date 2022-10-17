#!/usr/bin/python3
"""
    User class file for object creation
    and manipulation in HBnB console.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class implementation

        Attributes:
        email - string representing the user's email address
        password - string representing the user's password
        first_name - string representing the user's first name
        last_name - string representing the user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
