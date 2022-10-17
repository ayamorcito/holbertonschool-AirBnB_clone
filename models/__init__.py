#!/usr/bin/python3
"""
    Models initialization file.
    Reloads local storage files if existent,
    initializes empty storage if not.
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
cls_dict = {
    "BaseModel": BaseModel().__class__,
    "Amenity": Amenity().__class__,
    "City": City().__class__,
    "Place": Place().__class__,
    "Review": Review().__class__,
    "State": State().__class__,
    "User": User().__class__,
}