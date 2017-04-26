
import unittest

from dojo import Dojo


class TestsForTask0(unittest.TestCase):
    """
    Test cases for create_room and add_person functionalities
    """
    def test_create_room_successfully(self):
        """
        Test if a room is created successfully with the create_room method in Dojo
        """
        dojo = Dojo()
        initial_room_count = len(dojo.all_rooms)

        blue_office = dojo.create_room("office", "Blue")
        self.assertTrue(blue_office)

        new_room_count = len(dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

        no_office_created = dojo.create_room("blue", "office")
        self.assertFalse(no_office_created)

if __name__ == "__main__":
    unittest.main()
