
class Room(object):
    """
    A Room class that is used to create a room in the Dojo.
    This is the super class that is inherited by OfficeSpace and LivingSpace classes
    """
    def __init__(self, room_type, room_name):
        """
        This is the initializer of the class. room_name and room_type as passed in while
        initializing Room objects
        """
        self.__room_name = room_name
        self.__room_type = room_type
        self.__occupants=[]

    @property
    def room_name(self):
        """
        This is a getter for the room_name attribute.
        It's accessed using the instance of the Room object
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

        @property
    def occupants(self):
        """
        This is a getter for the occupants attribute of the Room object
        :return: occupants
        """
        return self.__occupants

    @room_type.setter
    def occupants(self, occupants):
        """
        This sets the occupants of the room
        :param occupants:
        :return:
        """

    def print_name(self, room_name):
        """
        Prints the name of the room passed and it's occupants
        Loops through the list of occupants and prints them out
        :param room_name:
        :return:
        """
        pass

"""
    def __eq__(self, other):
        
        Needed to compare if an office with the same name
        already exists in the available office list
        
        return self.__room_name == other.__room_name
        """
    