#!/usr/bin/python3
""" Testing city """
import unittest
import pep8
from models.city import City


class CityTesting(unittest.TestCase):
    """ Check City """

    def test_pep8(self):
        """ Test code style """
        pep8style = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = pep8style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
