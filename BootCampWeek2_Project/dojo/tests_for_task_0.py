
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

        duplicate_room = dojo.create_room("office", "Blue")
        self.assertEqual(duplicate_room, False)

    def test_add_person_successfully(self):
        """
        Test if a person is added successfully using the add_person method in Dojo
        """
        dojo = Dojo()
        initial_people_count = len(dojo.all_people)

        #add_person(self, person_name, person_type, wants_accommodation="N")

        staff_one = dojo.add_person("Stan Lee", "staff")
        self.assertTrue(staff_one)



if __name__ == "__main__":
    unittest.main()
