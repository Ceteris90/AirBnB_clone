#!/usr/bin/python3
"""
=================================
Unittest class for the base model
=================================
"""

# import module
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    ====================================
    Test BaseModel for Unittest TestCase
    ====================================

    Description:
        - Unittest model for BaseModel

    """
    def setUp(self):
        """
        ================================
        setup the model for the unittest
        ================================

        Description:
            - set the unittest for Base

        Args:
            -

        Return:
            -
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        ===================================
        Teardowm the model for the unittest
        ===================================

        Description:
            - Tear down the unittest for Base

        Args:
            -

        Return:
            -
        """
        del self.model

    def test_default_attributes(self):
        """
        ======================================
        set the default model for the unittest
        ======================================

        Description:
            - set the default test for Basemodel

        Args:
            -

        Return:
            -
        """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_setting_attributes(self):
        """
        ========================================
        setting the attribute for the base model
        ========================================

        Description:
            - set the attribute for the BaseModel

        Args:
            -

        Return:
            -
        """
        self.model.name = "John"
        self.assertEqual(self.model.name, "John")

    def test_to_dict_method(self):
        """
        ===================================
        setting the attribute to dictionary
        ===================================

        Description:
            -

        Args:
            -

        Return:
            -
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str_representation(self):
        """
        ================================================
        setting string representation for the base model
        ================================================

        Description:
            - setting the string representation for base

        Args:
            -

        Return:
            -
        """
        model_str = str(self.model)
        self.assertEqual(model_str, f"[BaseModel] ({self.model.id})\
                {self.model.__dict__}")

    def test_save_method(self):
        """
        ===========================================
        setting the save methmod for the base model
        ===========================================

        Description:
            - assert the save methmod for the base

        Args:
            -

        Return:
            -
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_created_at_and_updated_at(self):
        """
        =============================================
        setting the created_at and up_dated for model
        =============================================

        Description:
            - setting the created_at and updated_at

        Args:
            -

        Return:
            -
        """
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_init_with_args(self):
        """
        ========================================
        setting the init with args for the model
        ========================================

        Description:
            - created the init with args

        Args:
            -

        Return:
            -
        """
        id = '123'
        created_at = datetime.now()
        updated_at = datetime.now()
        model = BaseModel(id, created_at, updated_at)
        self.assertEqual(model.id, '123')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
        ===========================================
        setting the init for keywords for basemodel
        ===========================================

        Description:
            -

        Args.
            -

        Return:
            -
        """
        kwargs = {'name': 'John', 'age': 30}
        model = BaseModel(**kwargs)
        self.assertEqual(model.name, 'John')
        self.assertEqual(model.age, 30)


if __name__ == '__main__':
    unittest.main()
