"""Dojo Space Allocation
"""

from office_space import OfficeSpace
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff

class Dojo():
    """Dojo class which is the main class of the system. It calls and implements most of the
functionality needed in the system"""

    #def __init__(self):
    all_rooms = []
    all_people = []

    def create_room(self, room_type, room_name):
        """
        This creates a room and saves it in the Dojo all_rooms list.
        :param room_type, room_name:
        :return: Boolean
        """
        for room in self.all_rooms:
            if room.room_name == room_name:
                print("A room called " + room_name + " already exists. Choose another name")
                return False
        if room_type == "office":
            new_office = OfficeSpace(room_name)
            self.all_rooms.append(new_office)

            print("An office called " + room_name + " has been successfully created!")
            return True
        elif room_type == "livingspace":
            new_office = LivingSpace(room_name)
            self.all_rooms.append(new_office)

            print("A living space called " + room_name + " has been successfully created!")
            return True
        else:
            return False

    def add_person(self, person_name, person_type, wants_accommodation="N"):
        """Adds a person to the system and allocates the person a random room"""
        print(person_name + " " + person_type + " " + wants_accommodation)

        for person in self.all_people:
            print("A person called " + person_name + " already exists. Choose another name")
            return False
        if person_type == "fellow":
            if wants_accommodation == "Y":
                new_fellow = Fellow(person_name, True)
                #new_fellow.is_allocated(True)



if __name__ == '__main__':
    pass

