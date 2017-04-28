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
                print("\n\n\t\t\t---------------------------\n\n")

                return False
        if room_type == "office":
            new_office = OfficeSpace(room_name)
            self.all_rooms.append(new_office)

            print("An office called " + room_name + " has been successfully created!")
            print("\n\n\t\t\t---------------------------\n\n")

            return True
        elif room_type == "livingspace":
            new_office = LivingSpace(room_name)
            self.all_rooms.append(new_office)

            print("A living space called " + room_name + " has been successfully created!")
            print("\n\n\t\t\t---------------------------\n\n")

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
                print("\n\n\t\t\t---------------------------\n\n")

                return False
        if person_type == "fellow": #the person to add is a fellow
            if wants_accommodation == "Y": #the fellow wants an accommodation

                new_fellow = Fellow(first_name, second_name, True)

                print("Fellow " + first_name + " " + second_name + " has been successfully added.")
                print("\n\n\t\t\t---------------------------\n\n")

                if self.get_available_office_spaces():
                    #randomly retrieve an office space that is available
                    office_space = random.choice(self.get_available_office_spaces())
                    office_space.occupants.append(new_fellow) #add a person to the occupants list of the current office space

                    new_fellow.office_name = office_space.room_name

                    new_fellow.is_allocated = True

                    print(first_name + " has been allocated the office " + office_space.room_name)
                    print("\n\n\t\t\t---------------------------\n\n")

                else:
                    new_fellow.is_allocated = False

                if self.get_available_living_spaces():
                    #randomly retrieve a living space that is available
                    living_space = random.choice(self.get_available_living_spaces())
                    living_space.occupants.append(new_fellow) #add a person to the occupants list of the current living space

                    new_fellow.livingspace_name = living_space.room_name

                    new_fellow.is_allocated = True

                    print(first_name + " has been allocated the livingspace " + living_space.room_name)
                    print("\n\n\t\t\t---------------------------\n\n")

                else:
                    new_fellow.is_allocated = False

                self.all_people.append(new_fellow) #add the created person to the global list of all people

                return True

            else: #the fellow doesn't want accommodation

                new_fellow = Fellow(first_name, second_name, False)

                print("Fellow " + first_name + " " + second_name + " has been successfully added.")
                print("\n\n\t\t\t---------------------------\n\n")

                if self.get_available_office_spaces():

                    #randomly retrieve an office space that is available
                    office_space = random.choice(self.get_available_office_spaces())
                    office_space.occupants.append(new_fellow) #add a person to the occupants list of the current office space

                    new_fellow.office_name = office_space.room_name

                    new_fellow.is_allocated = True

                    print(first_name + " has been allocated the office " + office_space.room_name)
                    print("\n\n\t\t\t---------------------------\n\n")

                else:
                    new_fellow.is_allocated = False

                self.all_people.append(new_fellow) #add the created person to the global list of all people

                return True

        elif person_type == "staff": # the person to add is a staff

            new_staff = Staff(first_name, second_name)

            print("Staff " + first_name + " " + second_name + " has been successfully added.")
            print("\n\n\t\t\t---------------------------\n\n")

            if self.get_available_office_spaces():
                #randomly retrieve an office space that is available
                office_space = random.choice(self.get_available_office_spaces())
                office_space.occupants.append(new_staff) #add a person to the occupants list of the current office space

                new_staff.office_name = office_space.room_name

                new_staff.is_allocated = True

                print(first_name + " has been allocated the office " + office_space.room_name)                
                print("\n\n\t\t\t---------------------------\n\n")

            else:
                new_staff.is_allocated = False

            self.all_people.append(new_staff) #add the created person to the global list of all people

            return True

        else: #person_type entered is neither fellow nor staff. should not be allowed
            print("Wrong person type entered. Only 'staff' and 'fellow' are supported")
            print("\n\n\t\t\t---------------------------\n\n")

            return False

    def print_room(self, room_name):
        """Prints  the names of all the people in room_name on the screen.
        :param room_name:
        :return: List[]:Boolean
        """
        found_room = False #flag used to tell whether the entered room number actually exists

        for room in self.all_rooms: #loop through all already saved rooms to find what we need
            if room.room_name == room_name:
                room_occupants = room.occupants
                found_room = [True]

                if not room_occupants:
                    print("The room is empty")
                    print("\n\n\t\t\t---------------------------\n\n")
                    return [True]
                else:
                    for person in room_occupants:
                        print(person.first_name + " " + person.second_name)

                    return room_occupants

        if not found_room: #we didn't find the room
            print("The room name entered doesn't exist")
            print("\n\n\t\t\t---------------------------\n\n")

            return [False]

    def print_allocations(self, file_name=None):
        """Prints a list of allocations onto the screen.
        Specifying the optional file_name here outputs the registered allocations to a txt file.
        :param file_name:
        :return: List[]:Boolean
        """
        string_to_print = ""
        for room in self.all_rooms: #loop through the saved rooms and get their occupants
            if room.occupants: #the room has people
                string_to_print += room.room_name.upper() + "\n" + "----------------------------------------------"
                room_occupants = room.occupants
                occupants_names = []
                for occupant in room_occupants:
                    occupants_names.append(occupant.first_name + " " + occupant.second_name)
                string_to_print += ', '.join(occupants_names) + "\n\n"
            else:
                continue
        
        if (file_name == None): #no file name to write to. just print
            print(string_to_print)
        #else:
