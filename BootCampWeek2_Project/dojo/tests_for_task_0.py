"""
Test cases for create_room and add_person functionalities
"""
import unittest

from dojo.dojo import Dojo


class TestsForTask0(unittest.TestCase):
    def test_create_room_successfully(self):
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)
        blue_office = dojo.create_room("Blue", "office")
        self.assertTrue(blue_office)
        new_room_count = len(dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

if __name__ == "__main__":
    unittest.main()
