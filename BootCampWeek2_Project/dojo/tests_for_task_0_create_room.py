
import unittest

from dojo import Dojo

class TestsForTask0CreateRoom(unittest.TestCase):
    """
    Test cases for create_room functionalities
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_create_room_successfully(self):
        """
        Test if a room is created successfully with the create_room method in Dojo
        """
        blue_office = self.dojo.create_room("office", "Blue")
        self.assertTrue(blue_office)

    def test_create_room_added_to_list(self):
        """Test if the total room count increases after creating a room
        """
        initial_room_count = len(self.dojo.all_rooms)
        blue_office = self.dojo.create_room("office", "Blue")
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_bad_room_type_not_created(self):
        """Test that a room is not created when the room type is not office or livingspace
        """
        no_office_created = self.dojo.create_room("blue", "office")
        self.assertFalse(no_office_created)

    def test_duplicate_room_not_created(self):
        """Test that a room that has a name as an already created room is not created
        """
        love_space = self.dojo.create_room("livingspace", "Love")
        duplicate_room = self.dojo.create_room("livingspace", "Love")
        self.assertEqual(duplicate_room, False)


if __name__ == "__main__":
    unittest.main()
