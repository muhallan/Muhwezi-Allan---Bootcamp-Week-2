"""Dojo Space Allocation
"""

import random
from office_space import OfficeSpace
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff

class Dojo():
    """Dojo class which is the main class of the system. It calls and implements most of the
functionality needed in the system"""

    def __init__(self):
        """"The init method of Dojo. It initializes all_rooms list and all_people to empty
        """
        self.all_rooms = []
        self.all_people = []

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

    def get_available_office_spaces(self):
        """Get a list of office spaces that are not fully occupied
        :param
        :return: List[]
        """
        available_office_spaces = []
        for room in self.all_rooms:
            if isinstance(room, OfficeSpace): #get only rooms which are office spaces
                if len(room.occupants) < room.max_num_of_occupants: #check if this room is not full
                    available_office_spaces.append(room) #add that room to the list we will return

        return available_office_spaces

    def get_available_living_spaces(self):
        """Get a list of living spaces that are not fully occupied
        :param
        :return: List[]
        """
        available_living_spaces = []
        for room in self.all_rooms:
            if isinstance(room, LivingSpace): #get only rooms which are living spaces
                if len(room.occupants) < room.max_num_of_occupants: #check if this room is not full
                    available_living_spaces.append(room) #add that room to the list we will return

        return available_living_spaces

    def add_person(self, first_name, second_name, person_type, wants_accommodation="N"):
        """Adds a person to the system and allocates the person a random room
        :param person_name, person_type, wants_accommodation="N":
        :return: Boolean
        """
        for person in self.all_people:
            person_name = person.first_name + " " + person.second_name
            if person_name == first_name + " " + second_name:
                print("A person called " + person_name + " already exists. Choose another name")
                return False
        if person_type == "fellow": #the person to add is a fellow
            if wants_accommodation == "Y": #the fellow wants an accommodation

                new_fellow = Fellow(first_name, second_name, True)

                if self.get_available_office_spaces():
                    #randomly retrieve an office space that is available
                    office_space = random.choice(self.get_available_office_spaces())
                    office_space.occupants.append(new_fellow) #add a person to the occupants list of the current office space

                    new_fellow.office_name = office_space.room_name

                    new_fellow.is_allocated = True

                else:
                    new_fellow.is_allocated = False

                if self.get_available_living_spaces():
                    #randomly retrieve a living space that is available
                    living_space = random.choice(self.get_available_living_spaces())
                    living_space.occupants.append(new_fellow) #add a person to the occupants list of the current living space

                    new_fellow.livingspace_name = living_space.room_name

                    new_fellow.is_allocated = True

                else:
                    new_fellow.is_allocated = False

                self.all_people.append(new_fellow) #add the created person to the global list of all people

                return True

            else: #the fellow doesn't want accommodation

                new_fellow = Fellow(first_name, second_name, False)

                if self.get_available_office_spaces():

                    #randomly retrieve an office space that is available
                    office_space = random.choice(self.get_available_office_spaces())
                    office_space.occupants.append(new_fellow) #add a person to the occupants list of the current office space

                    new_fellow.office_name = office_space.room_name

                    new_fellow.is_allocated = True

                else:
                    new_fellow.is_allocated = False

                self.all_people.append(new_fellow) #add the created person to the global list of all people

                return True

        elif person_type == "staff": # the person to add is a staff

            new_staff = Staff(first_name, second_name)

            if self.get_available_office_spaces():
                #randomly retrieve an office space that is available
                office_space = random.choice(self.get_available_office_spaces())
                office_space.occupants.append(new_staff) #add a person to the occupants list of the current office space

                new_staff.office_name = office_space.room_name

                new_staff.is_allocated = True

            else:
                new_staff.is_allocated = False

            self.all_people.append(new_staff) #add the created person to the global list of all people

            return True

        else: #person_type entered is neither fellow nor staff. should not be allowed
            print("Wrong person type entered. Only 'staff' and 'fellow' are supported")
            return False


if __name__ == '__main__':
    pass

