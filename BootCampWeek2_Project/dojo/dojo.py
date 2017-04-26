"""Dojo Space Allocation
"""

from office_space import OfficeSpace
from living_space import LivingSpace


class Dojo():
    """Dojo class which is the main class of the system. It calls and implements most of the
functionality needed in the system"""

    #def __init__(self):
    all_rooms = []
    all_people = []

    def create_room(self, room_type, room_name):
        """
        This creates a room and saves it in the Dojo.
        :param room_type, room_name:
        :return: Boolean
        """
        if room_type == "office":
            new_office = OfficeSpace(room_name)
            self.all_rooms.append(new_office)

            print("An office called " + room_name + " has been successfully created!")
        elif room_type == "livingspace":
            new_office = LivingSpace(room_name)
            self.all_rooms.append(new_office)

            print("A living space called " + room_name + " has been successfully created!")

    def add_person(self, person_name):
        """Adds a person to the system and allocates the person a random room"""
        pass


if __name__ == '__main__':
    pass