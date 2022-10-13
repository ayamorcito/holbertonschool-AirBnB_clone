#!/usr/bin/python3
"""
    FileStorage class implementation for
    data manipulation (save/restore)
"""
import json
from os import path


class FileStorage():
    """
        FileStorage class implementation
        with data manipulation methods 
        (save/restore/serialization)
    """
    __file_path = "localStorage.json"
    __objects = {}

    def all(self):
        """
            Returns dictionary representation of
            all saved objects
        """
        return self.__objects

    def new(self, obj):
        """
            Saves or overwrites an existing
            object in class storage
        """
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        if obj_name not in self.__objects:
            self.__objects[obj_name] = obj
        else:
            self.__objects.update({obj_name: obj})

    def save(self):
        """
            Serializes the __objects dictionary
            to the JSON file path __file_path
        """
        js_str = json.dumps(self.__objects)
        with open(self.__file_path, 'w+', encoding="UTF-8") as l_st:
            l_st.write(js_str)

    def reload(self):
        """
            Deserializes the __objects dictionary
            from the JSON file path __file_path
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as l_st:
                rld = json.load(l_st)
                self.__objects = rld
