#!/usr/bin/python3
"""
    FileStorage class file for
    serialization and deserialization of
    HBnB console object manipulation.
"""
import json
from os import path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
        FileStorage class implementation,
        containing the respective class
        methods to manipulate local storage
        instances (save/restore/serialize).

        Class atributes:
        __file_path - string representation of
        the local storage file path.
        __objects - dictionary containing the
        stored objects.
            Format:
            {<class_name.id>: object}
    """
    __file_path = "localStorage.json"
    __objects = {}

    def all(self):
        """
            Returns dictionary representation of
            all the stored objects in the
            __objects class attribute.
        """
        return self.__objects

    def new(self, obj):
        """
            Creates a new element associated to
            obj's class, and saves it to the
            __objects class attribute.

            Returns new object's id.
        """
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        if obj_name not in self.__objects:
            self.__objects[obj_name] = obj
        else:
            self.__objects.update({obj_name: obj})

    def save(self):
        """
            Saves changes to the object collection
            to the previosuly defined localStorage
            instance via serialization.
        """
        obj_cp = self.__objects.copy()
        for key, value in obj_cp.items():
            try:
                obj_cp[key] = value.to_dict()
            except TypeError:
                if isinstance(value, dict):
                    obj_cp[key] = value
        with open(self.__file_path, 'w+', encoding="UTF-8") as l_st:
            json.dump(obj_cp, l_st)

    def delete(self, id):
        """
            Deletes an object from collection
            from the previosuly defined localStorage
            instance via serialization.
        """
        dkey = None
        obj_cp = self.__objects.copy()
        for key, value in obj_cp.items():
            if value.id == id:
                dkey = key
                del self.__objects[dkey]
            if dkey:
                self.save()
                return True
        return False

    def update(self, id, attr, value):
        """
            Updates an object from collection
            from the previosuly defined localStorage
            instance via serialization.
        """
        obj_cp = self.__objects.copy()
        for key, value in obj_cp.items():
            if value.id == id:
                self.__objects.update({attr: value})
                return True
        return False

    def reload(self):
        """
            Deserializes the object collection from
            the previosuly defined localStorage path
            and stores it into the __objects class
            attribute.

            If localStorage path doesn't exist, the
            function does nothing.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF-8") as l_st:
                rld = json.load(l_st)
                for key, value in rld.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
