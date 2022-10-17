#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):

    def test_user_created_at(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'created_at'), True)
        self.assertEqual(type(obj_ur.created_at), datetime)

    def test_user_updated_at(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'updated_at'), True)
        self.assertEqual(type(obj_ur.updated_at), datetime)

    def test_user_email(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'email'), True)
        self.assertEqual(type(obj_ur.email), str)

    def test_user_password(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'password'), True)
        self.assertEqual(type(obj_ur.password), str)

    def test_user_first_name(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'first_name'), True)
        self.assertEqual(type(obj_ur.first_name), str)

    def test_user_last_name(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'last_name'), True)
        self.assertEqual(type(obj_ur.last_name), str)

