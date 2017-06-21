import unittest

from dojo import Dojo


class TestsForTask2LoadPeople(unittest.TestCase):
    """
    Test cases for the load people functionality and method
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_if_filename_is_too_short(self):
        """Tests to see if the file name passed to be written is to short to be a valid txt file
        """
        file_name_entered = self.dojo.load_people("txt")
        self.assertEqual(file_name_entered, "short", msg="The file name entered is too short to be valid")

    def test_if_filename_does_not_end_with_txt(self):
        """
        Tests if a file name entered is not a valid text file since it doesn't end with .txt
        :return:
        """
        another_file_name = self.dojo.load_people("plain_text")
        self.assertEqual(another_file_name, "not txt file", msg="The file name entered doesn't end with .txt")

    def test_if_a_valid_file_name_is_used(self):
        """
        Tests to see if a valid text file name is recognized and written to
        :return:
        """
        valid_file = self.dojo.load_people("valid_file.txt")
        self.assertEqual(valid_file, "valid_file.txt")
