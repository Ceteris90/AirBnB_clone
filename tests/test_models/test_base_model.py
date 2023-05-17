#!/usr/bin/python3
""" Testing files """
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTesting(unittest.TestCase):
    """ Check BaseModel """

    def test_pep8(self):
        """ Test code style """
        pep8style = pep8.StyleGuide(quiet=True)
        files_to_check = [
            'models/base_model.py',
            'models/__init__.py',
            'models/engine/file_storage.py'
        ]
        result = pep8style.check_files(files_to_check)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseModel(unittest.TestCase):
    """ Test class for BaseModel """

    def tearDown(self):
        """ Delete json file """
        del self.test

    def setUp(self):
        """ Create instance """
        self.test = BaseModel()

    def test_attr_none(self):
        """ Test None attribute """
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_kwargs_constructor(self):
        """ Test id with data """
        dictionary = {'score': 100}

        object_test = BaseModel(**dictionary)
        self.assertTrue(hasattr(object_test, 'id'))
        self.assertTrue(hasattr(object_test, 'created_at'))
        self.assertTrue(hasattr(object_test, 'updated_at'))
        self.assertTrue(hasattr(object_test, 'score'))

    def test_str(self):
        """ Test string """
        dictionary = {
            'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
            'created_at': '2025-06-28T14:00:00.000001',
            '__class__': 'BaseModel',
            'updated_at': '2030-06-28T14:00:00.000001',
            'score': 100
        }

        object_test = BaseModel(**dictionary)
        out = "[{}] ({}) {}\n".format(
            type(object_test).__name__, object_test.id, object_test.__dict__
        )

    def test_to_dict(self):
        """ Test dictionary """
        object_test = BaseModel(score=300)
        n_dict = object_test.to_dict()

        self.assertEqual(n_dict['id'], object_test.id)
        self.assertEqual(n_dict['score'], 300)
        self.assertEqual(n_dict['__class__'], 'BaseModel')
        self.assertEqual(n_dict['created_at'], object_test.created_at.isoformat())
        self.assertEqual(n_dict['updated_at'], object_test.updated_at.isoformat())

        self.assertEqual(type(n_dict['created_at']), str)
        self.assertEqual(type(n_dict['updated_at']), str)

    def test_datetime(self):
        """ Test datetime """
        base1 = BaseModel()
        self.assertFalse(datetime.now() == base1.created_at)

    def test_BaseModel(self):
        """ Test attributes values in a BaseModel """
        my_model = BaseModel()
        my_model.name = "Holbie"
        my_model.my_number = 100
        my_model.save()
        my_model_json = my_model.to_dict()

        self.assertEqual(my_model.name, my_model_json['name'])
        self.assertEqual(my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(my_model.id, my_model_json['id'])

    def test_save_first(self):
        """ Test saving with invalid types """
        with self.assertRaises(AttributeError):
            BaseModel.save([455, 323232, 2323, 2323, 23332])
