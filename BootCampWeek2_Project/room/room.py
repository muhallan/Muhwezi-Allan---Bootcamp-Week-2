"""
A Room class that is used to create a room in the Dojo. This is the super class that is inherited by
"""


class Room (object):
    def __init__(self, room_name, room_type):
        """
        This is the initializer of the class. room_name and room_type as passed in while
        initializing Room objects
        """
        self.__room_name = room_name
        self.__room_type = room_type

    @property
    def room_name(self):
        """
        This is a getter for the room_name attribute. it's accessed using the instance of the Room object
        :return: room_name
        """
        return self.__room_name

    @room_name.setter
    def room_name(self, room_name):
        """
        This sets the passed value to the room_name attribute of the Room object
        :param room_name:
        :return:
        """

    @property
    def room_type(self):
        """
        This is a getter for the room_type attribute of the Room object
        :return: room_type
        """
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type):
        """
        This sets the passed string to the room_type attribute of the object
        :param room_type:
        :return:
        """

    def print_name(self, room_name, occupants):
        pass
