#!/usr/bin/python3
"""
    BaseModel class file for object creation
    and manipulation for the HBnB command console.

    Contains the BaseModel class and all its respective
    methods, documented in class docstring.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
        BaseModel class for HBnB objects.
        Unique ID assignement based on UUID4.

        Attributes:
        created_at - datetime object representing when an instance was created.
        updated_at - datetime object representing when an instance was updated.
    """

    def __init__(self, **kwargs):
        """
            Constructor function for BaseModel class.
        """
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key not in {'__class__', 'created_at', 'updated_at'}:
                    setattr(self, key, value)
                elif key in {'created_at', 'updated_at'}:
                    setattr(self, key, datetime.fromisoformat(value))

    def __str__(self):
        """
            Overloaded string method that prints
            a human-readable representation
            of the current instance object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            Saves changes to the current instance
            object to the current database.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary representation of
            the current instance object.
            '__class__' key is added when called,
            with class name as associated value.
        """
        my_dic = self.__dict__.copy()
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        my_dic["__class__"] = self.__class__.__name__
        return my_dic
