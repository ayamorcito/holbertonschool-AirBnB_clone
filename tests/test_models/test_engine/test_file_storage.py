#!/usr/bin/python3

import unittest
import models
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ test to class FileStorage """


    def test_all(self):
        """ test .all generates dict """
        self.assertEqual(type(models.storage.all()), dict)

    def test_save(self):
        pass

    def test_new(self):
        """ test the creation of different instances """
        b = BaseModel()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        u = User()

        models.storage.new(b)
        models.storage.new(s)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(p)
        models.storage.new(r)
        models.storage.new(u)

        self.assertIn(f'{b.__class__.__name__}.{b.id}',
                      models.storage.all().keys())
        self.assertIn(f'{s.__class__.__name__}.{s.id}',
                      models.storage.all().keys())
        self.assertIn(f'{c.__class__.__name__}.{c.id}',
                      models.storage.all().keys())
        self.assertIn(f'{a.__class__.__name__}.{a.id}',
                      models.storage.all().keys())
        self.assertIn(f'{p.__class__.__name__}.{p.id}',
                      models.storage.all().keys())
        self.assertIn(f'{r.__class__.__name__}.{r.id}',
                      models.storage.all().keys())
        self.assertIn(f'{u.__class__.__name__}.{u.id}',
                      models.storage.all().keys())
