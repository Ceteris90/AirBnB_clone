#!/usr/bin/python3
"""
========================
Class of Reiew the model
========================
"""

# import the module
import unittest
from models.review import Review


class TestPlace(unittest.TestCase):
    """
    ============================
    unittest for the reiew class
    ============================

    Description:
        - class for the unittest
    """

    def setUp(self):
        """
        =================================
        set up the place for the unittest
        =================================

        Description:
            - use for setting up the review

        Args:
            -

        Return:
            -
        """

        self.reiew = Review()

    def tearDown(self):
        """
        ========================================
        tear down of the review for the unittest
        ========================================

        Description:
            - tear down setting up the review

        Args:
            -

        Return:
            -
        """

        del self.review

    def test_default_attributes(self):
        """
        ===========================================
        test for the default value for the unittest
        ===========================================

        Description:
            - assert the default setup of the review

        Args:
            -

        Return:
            -
        """

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_setting_attributes(self):
        """
        ===================================
        test for the value for the unittest
        ===================================

        Description:
            - set the review

        Args:
            -

        Return:
            -
        """
        self.review.place_id = "1234-abcd"
        self.review.user_id = "1234-abcd"
        self.review.text = "A very bad bathroom"
        self.assertEqual(self.review.place, "1234-abcd")
        self.assertEqual(self.review.user_id, "1234-abcd")
        self.assertEqual(self.review.text, "A very bad bathroom")

    def test_to_dict_method(self):
        """
        ===================================
        test asset or convert to dictionary
        ===================================

        Description:
            - set the review to dict

        Args:
            -

        Return:
            -
        """
        review_dict = self.place.to_dict()
        self.assertEqual(review_dict["place_id"], "")
        self.assertEqual(review_dict["user_id"], "")
        self.assertEqual(review_dict["text"], "")

    def test_str_representation(self):
        """
        ========================================
        set the string of review for the unittest
        ========================================

        Description:
            - string representation up

        Args:
            -

        Return:
            -
        """
        expected_str = "[Review] (1234-abcd) {}"\
            .format(self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)


if __name__ == "__main__":
    unittest.main()
