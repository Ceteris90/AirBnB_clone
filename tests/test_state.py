#!/usr/bin/python3
"""
=======================
unitest for state class
=======================
"""

# import module
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    ===============================
    State class unittest TestCase
    ===============================

    Description:
        - State class unittest test
    """

    def setUp(self):
        """
        ==============================
        set up the state class of user
        ==============================
        
        Description:
            - seting up the state class
        Args:
            -
        Return:
            -
        """
        self.state = State()

    def tearDown(self):
        """
        =================================
        tear down the state class of user
        =================================

        Description:
            - tear down the state class
        Args:
            -
        Return:
            -
        """
        del self.state

    def test_default_attributes(self):
        """
        ==============================
        test the state class of user
        ==============================
        
        Description:
            - set the state class
        Args:
            -
        Return:
            -
        """
        self.assertEqual(self.state.name, "")

    def test_setting_attributes(self):
        """
        ==============================
        Assert the state class of user
        ==============================

        Description:
            - assert the state input
        Args:
            -
        Return:
            -
        """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_to_dict_method(self):
        """
        =========================================
        set to dictionary the state class of user
        =========================================

        Description:
            - set the state to dictionary
        Args:
            -
        Return:
            -
        """
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["name"], "")

    def test_str_representation(self):
        """
        ==============================
        set up the state class of user
        ==============================

        Description:
            - seting up the state class
        Args:
            -
        Return:
            -
        """
        expected_str = "[State] (1234-abcd) {}"\
            .format(self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)


if __name__ == '__main__':
    unittest.main()
