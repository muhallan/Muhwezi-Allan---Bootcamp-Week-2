import unittest

from dojo import Dojo

class TestsForTask1PrintRoom(unittest.TestCase):
    """Test cases for the print_room method and functionality
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_room_name_exists(self):
        """Tests if there is an already created room with the given name
        """
        exists = dojo.print_room("allan")
        self.assertTrue(exists)