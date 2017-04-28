import unittest

from dojo import Dojo
from person import Person

class TestsForTask1PrintRoom(unittest.TestCase):
    """Test cases for the print_room method and functionality
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_room_name_not_exists(self):
        """Tests if there is an already created room with the given name
        """
        allan_office = self.dojo.create_room("office", "allan")
        exists = self.dojo.print_room("jumbo")
        self.assertListEqual(exists, [False], msg="should return a list containing False")

    def test_get_list_of_names(self):
        """Tests to see if it prints a list of people's names that are in a room
        """
        test_livingspace = self.dojo.create_room("livingspace", "test")

        allan = Person("allan", "great")
        john = Person("john", "doe")
        mark = Person("mark", "alvin")

        people = [allan, john, mark]

        self.dojo.all_rooms[0].occupants = people #assigned the people to the room's occupants

        self.assertListEqual(people, self.dojo.print_room("test"), msg="list of names found and printed")

if __name__ == "__main__":
    unittest.main()
