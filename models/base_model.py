#!/usr/bin/python3
""" All hail BaseModel, first of her name, mother of classes, ruler of the console """

from datetime import datetime
import uuid


class BaseModel():
    """ First Class for others to inherit from """
    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ prints the str """
        return(f"[self.__class__.__name__] (self.id) self.__dic__")

    def save(self):
        """ updates the atribute with the current datetime """
        self.updated_at = datetime.now

    def to_dict(self):
        """ returns a dictionary containing keys/values of instance """
        my_dic = self.__dict__.copy()
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.created_at.isoformat()
        my_dic["__class__"] = self.__class__.__name__
        return my_dic
