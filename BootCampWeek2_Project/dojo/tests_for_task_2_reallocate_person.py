import unittest

from dojo import Dojo


class TestsForTask2ReallocatePerson(unittest.TestCase):
    """
    Test cases for the reallocate_room method and functionality
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_reallocate_to_no_non_existent_room(self):
        """"
        Test if reallocating to a room that doesn't exist fails with a message
        """
        no_room = self.dojo.reallocate_person("one", "two", "non_existent")
        self.assertEqual(no_room, "no_room")

    def test_if_available_room_is_reallocated_to(self):
        """
        Test if an available room to be reallocated to is actually found
        :return:
        """
        self.dojo.create_room("livingspace", "my_room")
        self.dojo.reallocate_person("fName", "lName", "my_room")
        self.assertEqual(self.dojo.all_rooms[-1].room_name, "my_room")  # the last entered room is found

    def test_reallocate_to_non_existent_person(self):
        """
        Test if reallocating to a person who is not in the system fails
        :return:
        """
        self.dojo.create_room("livingspace", "my_room")
        no_person = self.dojo.reallocate_person("romain", "guy", "my_room")
        self.assertEqual(no_person, "no_person", msg="Should return no_person")

    def test_reallocate_to_an_unallocated_person(self):
        """
        Test if reallocating a person who has not been fully allocated before
        :return:
        """
        self.dojo.create_room("livingspace", "my_space")
        self.dojo.add_person("welike", "elly", "fellow", "y")
        unallocated = self.dojo.reallocate_person("welike", "elly", "my_space")
        self.assertEqual(unallocated, "unallocated_person")

    def test_reallocate_an_allocated_person(self):
        """
        Test if a fully allocated person is found and the room entered is also found
        :return:
        """
        self.dojo.create_room("office", "my_office")
        self.dojo.add_person("john", "ike", "staff")
        self.dojo.reallocate_person("john", "ike", "my_office")
        self.assertEqual(self.dojo.all_people[-1].is_allocated, True)

    def test_cant_move_staff_to_living_space(self):
        """
        Test if Staff can't be reallocated to a living space room
        :return:
        """
        self.dojo.create_room("livingspace", "my_space")
        self.dojo.create_room("office", "my_office")
        self.dojo.add_person("john", "ike", "staff")
        no_living_space = self.dojo.reallocate_person("john", "ike", "my_space")
        self.assertEqual(no_living_space, "staff_no_living_space")

    def test_reallocate_to_the_same_room(self):
        """
        Test if the room to reallocate to is the same as what the person is already assigned to
        :return:
        """
        self.dojo.create_room("livingspace", "my_space")
        self.dojo.create_room("office", "my_office")
        self.dojo.add_person("john", "ike", "staff")
        same_room = self.dojo.reallocate_person("john", "ike", "my_office")
        self.assertEqual(same_room, "same_room")

    def test_if_person_has_been_moved_from_the_former_room(self):
        """
        Test the number of occupants of the old room have been reduced by 1
        :return:
        """
        self.dojo.create_room("office", "my_first_office")
        self.dojo.add_person("john", "ike", "staff")
        first_office_occupants_number_before = len(self.dojo.all_rooms[0].occupants)
        self.dojo.create_room("office", "my_second_office")
        self.dojo.reallocate_person("john", "ike", "my_second_office")
        first_office_occupants_number_after = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual(first_office_occupants_number_before - first_office_occupants_number_after, 1)

    def test_if_person_has_been_added_to_the_new_room(self):
        """
        Test if the number of occupants of the room moved to has increased by 1
        :return:
        """
        self.dojo.create_room("office", "my_first_office")
        self.dojo.add_person("john", "ike", "staff")
        self.dojo.create_room("office", "my_second_office")
        second_office_occupants_number_before = len(self.dojo.all_rooms[1].occupants)
        self.dojo.reallocate_person("john", "ike", "my_second_office")
        second_office_occupants_number_after = len(self.dojo.all_rooms[1].occupants)
        self.assertEqual(second_office_occupants_number_after - second_office_occupants_number_before, 1)

    def test_if_function_runs_successfully_as_expected(self):
        """
        Test if the expected strings are returned from each conditions
        :return:
        """
        self.dojo.create_room("office", "my_first_office")
        self.dojo.add_person("john", "ike", "staff")
        self.dojo.create_room("office", "my_second_office")
        string_expected = self.dojo.reallocate_person("john", "ike", "my_second_office")
        self.assertEqual(string_expected, "my_second_office, john ike, staff, office, my_first_office")
