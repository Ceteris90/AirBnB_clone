#!/usr/bin/python3
"""
========================================
Test Amenity that inherite from Unittest
========================================
"""

# import module
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    ===================================
    class for the Test Amenity unittest
    ===================================

    Description:
        - class for amenity test
    """
    def setUp(self):
        """
        ===================================
        Setup for the Test Amenity unittest
        ===================================

        Description:
            - setup class for amenity test

        Args:
            -

        Return:
            -
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        ===================================
        tear down for Test Amenity unittest
        ===================================

        Description:
            - tear down for amenity test

        Args:
            -

        Return:
            -
        """
        del self.amenity

    def test_default_attributes(self):
        """
        =====================================
        default for the Test Amenity unittest
        =====================================

        Description:
            - default class for amenity test

        Args:
            -

        Return:
            -
        """
        self.assertEqual(self.amenity.name, "")

    def test_setting_attributes(self):
        """
        ===================================
        Setting for the Test Amenity unittest
        ===================================

        Description:
            - setup class for amenity test

        Args:
            -

        Return:
            -
        """
        self.amenity.name = "WiFi"
        self.amenity.name = "swimming pool"
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertEqual(self.amenity.name, "swimming pool")

    def test_to_dict_method(self):
        """
        ===================================
        Setting for the Test Amenity unittest
        ===================================

        Description:
            - dict class for amenity test

        Args:
            -

        Return:
            -
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "")

    def test_str_representation(self):
        """
        ===================================
        string for the Test Amenity unittest
        ===================================

        Description:
            - string class for amenity test

        Args:
            -

        Return:
            -
        """
        expected_str = "[Amenity] (1234-abcd) {}"\
            .format(self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
