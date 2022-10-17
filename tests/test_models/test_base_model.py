#!/usr/bin/python3
"""
Unittest for base_model
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def test_base_model(self):
        """testing basic stuff for a base model obj"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        # checking attribute types and class
        self.assertEqual(type(my_model), BaseModel)
        # id
        self.assertTrue(hasattr(my_model, "id"))
        self.assertEqual(type(my_model.id), str)
        # created
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertEqual(type(my_model.created_at), datetime)
        # updated
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_save(self):
        """testing save"""
        obj_1 = BaseModel()
        created1 = obj_1.created_at
        updated1 = obj_1.updated_at
        obj_1.save()
        created2 = obj_1.created_at
        updated2 = obj_1.updated_at

        self.assertEqual(created1, created2)
        self.assertNotEqual(updated1, updated2)

    def test_str(self):
        """testing str method"""
        model = BaseModel()
        model_str = '[{}] ({}) {}'.format(
                BaseModel.__name__, model.id, model.__dict__)
        self.assertEqual(model_str, str(model))

    def test_docstring(self):
        """function to check docstring fo Basemodel"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_dict(self):
        """testing to dict function"""
        test = BaseModel()
        my_model = test.to_dict()
        self.assertTrue(type(my_model["created_at"] == str))
        self.assertTrue(type(my_model["updated_at"] == str))
        self.assertTrue(type(test.created_at) == datetime)
        self.assertTrue(type(test.updated_at) == datetime)
        self.assertEqual(my_model["created_at"], test.created_at.isoformat())
        self.assertEqual(my_model["updated_at"], test.updated_at.isoformat())

