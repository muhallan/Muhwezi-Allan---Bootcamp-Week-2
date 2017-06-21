import unittest

from dojo import Dojo

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

    def test_if_person_is_assigned_an_office(self):
        """Test and see if a person is created when there is an available office, that person is assigned to the office
        """
        sample_living = self.dojo.create_room("livingspace", "sample")
        fellow_one = self.dojo.add_person("Jumped", "Out", "fellow", "Y")
        self.assertTrue(self.dojo.all_people[0].is_allocated)

    def test_person_with_unknown_person_type_not_created(self):
        """Test if a person with person type not fellow or staff is not added
        """
        alien_person = self.dojo.add_person("Jim", "Kim", "star")
        self.assertFalse(alien_person)

    def test_staff_not_assigned_living_space(self):
        """Test if only a livingspace room is available and a staff is added, whether the staff will be assigned the livingspace room
        """
        sample_living = self.dojo.create_room("livingspace", "sample")
        unallocated_staff = self.dojo.add_person("Mr", "John", "staff")
        self.assertFalse(self.dojo.all_people[0].is_allocated)
