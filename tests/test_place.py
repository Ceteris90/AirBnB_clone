#!/usr/bin/python3
"""
============================
unittest for the place class
============================
"""

# import module
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
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
        set up the place for the unittest
        =================================

        Description:
            - use for setting up the place

        Args:
            -

        Return:
            _
        """

        self.place = Place()

    def tearDown(self):
        """
        ====================================
        tear down the place for the unittest
        ====================================

        Description:
            - tear down setting up the place

        Args:
            -

        Return:
            _
        """
        del self.place

    def test_default_attributes(self):
        """
        ===================================
        test as. the place for the unittest
        ===================================

        Description:
            - assert set up the place

        Args:
            -

        Return:
            _
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

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
        self.place.name = "Cozy Cabin"
        self.place.number_rooms = 2
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.number_rooms, 2)

    def test_to_dict_method(self):
        """
        =================================
        test assert conver to dictionary
        =================================

        Description:
            - set the place to dict

        Args:
            -

        Return:
            _
        """
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["city_id"], "")
        self.assertEqual(place_dict["user_id"], "")
        self.assertEqual(place_dict["name"], "")

    def test_str_representation(self):
        """
        =====================================
        set the str of place for the unittest
        =====================================

        Description:
            - string representation up place

        Args:
            -

        Return:
            _
        """
        expected_str = "[Place] (1234-abcd) {}"\
            .format(self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)


if __name__ == '__main__':
    unittest.main()
