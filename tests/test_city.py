#!/usr/bin/python3
"""
============================
Test class for City TestCase
============================
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    ============================
    unittest for the place class
    ============================

    Description:
        - class fo the unittest
    """

    def setUp(self):
        """
        =================================
        set up the city for the unittest
        =================================

        Description:
            - use for setting up the city

        Args:
            -

        Return:
            _
        """
        self.city = City()

    def tearDown(self):
        """
        ====================================
        tear down the city for the unittest
        ====================================

        Description:
            - tear down setting up the city

        Args:
            -

        Return:
            _
        """
        del self.city

    def test_default_attributes(self):
        """
        ===================================
        test def the place for the unittest
        ===================================

        Description:
            - assert set up the place

        Args:
            -

        Return:
            _
        """
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_setting_attributes(self):
         """
        ===================================
        test as. the place for the unittest
        ===================================

        Description:
            - set up the place

        Args:
            -

        Return:
            _
        """
        self.city.name = "New York"
        self.city.state_id = "1234-abcd"
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.state_id, "1234-abcd")

    def test_to_dict_method(self):
         """
        =================================
        test assert convert to dictionary
        =================================

        Description:
            - set the city to dict

        Args:
            -

        Return:
            _
        """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["name"], "")
        self.assertEqual(city_dict["state_id"], "")

    def test_str_representation(self):
        """
        =====================================
        set the str of city for the unittest
        =====================================

        Description:
            - string representation up city

        Args:
            -

        Return:
            _
        """
        expected_str = "[City] (1234-abcd) {}"\
            .format(self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()

