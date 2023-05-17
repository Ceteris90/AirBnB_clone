#!/usr/bin/python3
""" Testing State """
import unittest
import pep8
from models.state import State


class StateTesting(unittest.TestCase):
    """ Check State """

    def test_pep8(self):
        """ Test code style """
        pep8style = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pep8style.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
