#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_class(self):
        """ test for class and instance """
        obj_am = Amenity()

        self.assertEqual(obj_am.__class__, Amenity)

    def test_id(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'id'), True)
        self.assertEqual(type(obj_am.id), str)

    def test_created_at(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'created_at'), True)
        self.assertEqual(type(obj_am.created_at), datetime)

    def test_updated_at(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'updated_at'), True)
        self.assertEqual(type(obj_am.updated_at), datetime)

    def test_name(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'name'), True)
        self.assertEqual(type(obj_am.name), str)
