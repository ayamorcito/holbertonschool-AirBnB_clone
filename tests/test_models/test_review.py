#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.review import Review
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_class(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertEqual(obj_re.__class__, Review)

    def test_id(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'id'), True)
        self.assertEqual(type(obj_re.id), str)

    def test_created_at(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'created_at'), True)
        self.assertEqual(type(obj_re.created_at), datetime)

    def test_updated_at(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'updated_at'), True)
        self.assertEqual(type(obj_re.updated_at), datetime)

    def test_place_id(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'place_id'), True)
        self.assertEqual(type(obj_re.place_id), str)

