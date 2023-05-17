#!/usr/bin/python3
""" Check FileStorage class """
import unittest
from os import remove, path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """ Check the class """

    def setUp(self):
        """ Check empty """
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Check remove class """
        try:
            remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        """ Check empty class """
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """ Check all function """
        storage_instance = FileStorage()
        obj = storage_instance.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage_instance._FileStorage__objects)

    def test_save_create(self):
        """ Test save """
        classes = [BaseModel, User, City, Amenity, Place, Review, State]
        for cls in classes:
            obj = cls()
            obj_key = f'{cls.__name__}.{obj.id}'
            self.assertEqual(obj, storage.all()[obj_key])

    def test_new_empty(self):
        """ Check new method """
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_classes(self):
        """ Check new method is valid """
        classes = [BaseModel, User, City, Amenity, Place, Review, State]
        for cls in classes:
            obj = cls(id='123')
            obj_key = f'{cls.__name__}.{obj.id}'
            self.assertEqual(storage.all(), {})
            storage.new(obj)
            self.assertEqual(obj, storage.all()[obj_key])
