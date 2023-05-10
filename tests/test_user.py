#!/usr/bin/python3
"""
============================
Unittest for the User module
============================
"""
# import important modules
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    ==============================
    Unit tests for the User class.
    ==============================

    Description:
        - Class that create test
        - for the user class
    """

    def setUp(self):
        """
        ====================
        Set up test objects.
        ====================

        Description:
            - Setup the teset

        Args:
            -

        Return:
            -
        """
        self.user = User()

    def tearDown(self):
        """
        =========================
        Clean up after each test.
        =========================

        Description:
            - clean for a new test

        Args:
            -

        Return:
            -
        """
        del self.user

    def test_default_attributes(self):
        """
        ===============================================
        Test default attributes of a new User instance.
        ===============================================

        Description:
            - Test the default of the user instance

        Args:
            -

        Return:
            -
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_setting_attributes(self):
        """
        ===========================================
        Test setting attributes of a User instance.
        ===========================================

        Description:
            - Test the setting of the user instance

        Args:
            -

        Return:
            -
        """
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict_method(self):
        """
        ===========================================
        Test the to_dict method of a User instance.
        ===========================================

        Description:
            - Test the to_dict of the user instance

        Args:
            -

        Return:
            -
        """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)
        self.assertEqual(user_dict["__class__"], "User")

    def test_str_representation(self):
        """
        ==================================================
        Test the string representation of a User instance.
        ==================================================
        Description:
            - Test the strg repres. of the user instance

        Args:
            -

        Return:
            -
        """
        user_str = str(self.user)
        self.assertTrue("[User]" in user_str)
        self.assertTrue(self.user.id in user_str)


if __name__ == "__main__":
    unittest.main()
