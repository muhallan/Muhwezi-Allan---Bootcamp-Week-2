
import unittest

from dojo import Dojo


class TestsForTask0CreateRoom(unittest.TestCase):
    """
    Test cases for create_room functionalities
    """

    def setUp(self):
        """Initialize the test case class"""
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

class TestsForTask0AddPerson(unittest.TestCase):
    """Test cases for add_person functionalities
    """

    def setUp(self):
        """Initialize the test case class"""
        self.dojo = Dojo()

    def test_add_person_successfully(self):
        """
        Test if a person is added successfully using the add_person method in Dojo
        """
        staff_one = self.dojo.add_person("Stan", "Lee", "staff")
        self.assertTrue(staff_one)

    def test_create_room_added_to_list(self):
        """Test if the total people count increases after creating a people
        """
        initial_people_count = len(self.dojo.all_people)
        staff_one = self.dojo.add_person("Stan", "Lee", "staff")
        new_people_count = len(self.dojo.all_people)
        self.assertEqual(new_people_count - initial_people_count, 1)

    def test_duplicate_person_not_created(self):
        """Test that a person that has a name as an already created person is not created
        """
        staff_one = self.dojo.add_person("Stan", "Lee", "staff")
        staff_duplicate = self.dojo.add_person("Stan", "Lee", "staff")
        self.assertEqual(staff_duplicate, False)




if __name__ == "__main__":
    unittest.main()
