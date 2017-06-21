"""Dojo Space Allocation
"""

import random
from office_space import OfficeSpace
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff
from database import Database

class Dojo():
    """Dojo class which is the main class of the system. It calls and implements most of the
functionality needed in the system"""

    def __init__(self):
        """"The init method of Dojo. It initializes all_rooms list and all_people list to empty
        """
        self.all_rooms = []
        self.all_people = []

    def create_room(self, room_type, room_name):
        """
        This creates a room and saves it in the Dojo all_rooms list.
        :param room_type
        :param room_name:
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
            if isinstance(room, OfficeSpace):  # get only rooms which are office spaces
                if len(room.occupants) < room.max_num_of_occupants:  # check if this room is not full
                    available_office_spaces.append(room)  # add that room to the list we will return

        return available_office_spaces

    def get_available_living_spaces(self):
        """Get a list of living spaces that are not fully occupied
        :param
        :return: List[]
        """
        available_living_spaces = []
        for room in self.all_rooms:
            if isinstance(room, LivingSpace):  # get only rooms which are living spaces
                if len(room.occupants) < room.max_num_of_occupants:  # check if this room is not full
                    available_living_spaces.append(room)  # add that room to the list we will return

        return available_living_spaces

    def add_person(self, first_name, second_name, person_type, wants_accommodation="N"):
        """Adds a person to the system and allocates the person a random room
        :param first_name:
        :param second_name:
        :param person_type:
        :param wants_accommodation:
        :return: Boolean
        """

        for person in self.all_people:
            person_name = person.first_name + " " + person.second_name
            if person_name == first_name + " " + second_name:
                print("A person called " + person_name + " already exists. Choose another name")
                print("\n\n\t\t\t---------------------------\n\n")

                return False
        if person_type.lower() == "fellow":  # the person to add is a fellow
            if wants_accommodation == "Y":  # the fellow wants an accommodation

                new_fellow = Fellow(first_name, second_name, True)

                print("Fellow " + first_name + " " + second_name + " has been successfully added.")
                print("\n\n\t\t\t---------------------------\n\n")

                if self.get_available_office_spaces():
                    # randomly retrieve an office space that is available
                    office_space = random.choice(self.get_available_office_spaces())

                    # add a person to the occupants list of the current office space
                    office_space.occupants.append(new_fellow)

                    new_fellow.office_name = office_space.room_name

                    new_fellow.is_allocated = True

                    print(first_name + " has been allocated the office " + office_space.room_name)
                    print("\n\n\t\t\t---------------------------\n\n")

                else:
                    new_fellow.is_allocated = False

                if self.get_available_living_spaces():
                    # randomly retrieve a living space that is available
                    living_space = random.choice(self.get_available_living_spaces())

                    # add a person to the occupants list of the current living space
                    living_space.occupants.append(new_fellow)

                    new_fellow.livingspace_name = living_space.room_name

                    new_fellow.is_allocated = True

                    print(first_name + " has been allocated the livingspace " + living_space.room_name)
                    print("\n\n\t\t\t---------------------------\n\n")

                else:
                    new_fellow.is_allocated = False

                self.all_people.append(new_fellow)  # add the created person to the global list of all people

                return True

            else:  # the fellow doesn't want accommodation

                new_fellow = Fellow(first_name, second_name, False)

                print("Fellow " + first_name + " " + second_name + " has been successfully added.")
                print("\n\n\t\t\t---------------------------\n\n")

                if self.get_available_office_spaces():

                    # randomly retrieve an office space that is available
                    office_space = random.choice(self.get_available_office_spaces())

                    # add a person to the occupants list of the current office space
                    office_space.occupants.append(new_fellow)

                    new_fellow.office_name = office_space.room_name

                    new_fellow.is_allocated = True

                    print(first_name + " has been allocated the office " + office_space.room_name)
                    print("\n\n\t\t\t---------------------------\n\n")

                else:
                    new_fellow.is_allocated = False

                self.all_people.append(new_fellow)  # add the created person to the global list of all people

                return True

        elif person_type.lower() == "staff":  # the person to add is a staff

            new_staff = Staff(first_name, second_name)

            print("Staff " + first_name + " " + second_name + " has been successfully added.")
            print("\n\n\t\t\t---------------------------\n\n")

            if self.get_available_office_spaces():
                # randomly retrieve an office space that is available
                office_space = random.choice(self.get_available_office_spaces())

                # add a person to the occupants list of the current office space
                office_space.occupants.append(new_staff)

                new_staff.office_name = office_space.room_name

                new_staff.is_allocated = True

                print(first_name + " has been allocated the office " + office_space.room_name)
                print("\n\n\t\t\t---------------------------\n\n")

            else:
                new_staff.is_allocated = False

            self.all_people.append(new_staff)  # add the created person to the global list of all people

            return True

        else:  # person_type entered is neither fellow nor staff. should not be allowed
            print("Wrong person type entered. Only 'staff' and 'fellow' are supported")
            print("\n\n\t\t\t---------------------------\n\n")

            return False

    def print_room(self, room_name):
        """Prints  the names of all the people in room_name on the screen.
        :param room_name:
        :return: List[]:Boolean
        """
        found_room = False  # flag used to tell whether the entered room number actually exists
        room_occupants = []
        for room in self.all_rooms:  # loop through all already saved rooms to find what we need
            if room.room_name == room_name:
                room_occupants = room.occupants
                found_room = True
                break

        if found_room:
            if not room_occupants:
                print("The room is empty")
                print("\n\n\t\t\t---------------------------\n\n")
                return [True]
            else:
                for person in room_occupants:
                    print(person.first_name + " " + person.second_name)

                return room_occupants

        else:  # we didn't find the room
            print("The room name entered doesn't exist")
            print("\n\n\t\t\t---------------------------\n\n")

            return [False]

    def print_allocations(self, file_name=None):
        """Prints a list of allocations onto the screen.
        Specifying the optional file_name here outputs the registered allocations to a txt file.
        :param file_name:
        :return: String
        """
        string_to_print = ""
        for room in self.all_rooms:  # loop through the saved rooms and get their occupants
            if room.occupants:  # the room has people
                string_to_print += room.room_name.upper() + "\n" + "----------------------------------------------\n"
                room_occupants = room.occupants
                occupants_names = []
                for occupant in room_occupants:
                    occupants_names.append(occupant.first_name + " " + occupant.second_name)
                string_to_print += ', '.join(occupants_names) + "\n\n"
            else:
                continue

        print(string_to_print)

        if file_name is not None:  # no file name to write to. just print
            if len(file_name) < 4:
                return "short"
            elif file_name.split(".")[-1] != "txt":
                return "not txt file"
            else:
                try:
                    with open(file_name, "w+") as file_to_write:
                        file_to_write.write(string_to_print)
                except IOError:
                    print('Failed to write to the file provided')
                    print("\n\n\t\t\t---------------------------\n\n")

        return file_name

    def print_unallocated(self, file_name=None):
        """Prints a list of unallocated people to the screen.
        Specifying the filename here outputs the information to the txt file provided
        :param file_name:
        :return: String
        """
        string_to_print = ""
        for person in self.all_people:  # loop through the saved people
            if not person.is_allocated:  # if a person is not allocated fully print them out
                string_to_print += person.first_name + " " + person.second_name + "\n"
            else:
                continue

        print(string_to_print)

        if file_name is not None:  # no file name to write to. just print
            if len(file_name) < 4:
                return "short"
            elif file_name.split(".")[-1] != "txt":
                return "not txt file"
            try:
                with open(file_name, "w+") as file_to_write:
                    file_to_write.write(string_to_print)
            except IOError:
                print('Failed to write to the file provided')
                print("\n\n\t\t\t---------------------------\n\n")

        return file_name

    def reallocate_person(self, first_name, second_name, room_name):
        """Reallocate the person with person_identifier to new_room_name.
        :param first_name:
        :param second_name:
        :param room_name:
        :return: String
        """

        # declare a string to return and use in nosetests
        string_to_return = ""

        # check if the entered room_name is among the available ones
        available_living_spaces = self.get_available_living_spaces()
        available_office_spaces = self.get_available_office_spaces()

        all_available_rooms = []
        all_available_rooms.extend(available_living_spaces)
        all_available_rooms.extend(available_office_spaces)

        room_to_change_to = None
        found_room = False
        for room in all_available_rooms:
            if room.room_name == room_name:  # the room is available
                room_to_change_to = room
                found_room = True
                string_to_return += room_name
                break

        if not found_room:  # the room is not available
            print("The room you have entered is not available to add to.")
            print("\n\n\t\t\t---------------------------\n\n")
            return "no_room"

        found_person = False
        person_to_move = None
        for person in self.all_people:
            person_name = person.first_name + " " + person.second_name
            given_name = first_name + " " + second_name
            if person_name == given_name:  # the person has been found
                found_person = True
                person_to_move = person
                break

        if found_person:
            if not person_to_move.is_allocated:  # person is not allocated
                print("The person you have entered is not allocated to a room")
                print("\n\n\t\t\t---------------------------\n\n")
                return "unallocated_person"
            else:
                string_to_return += ", " + person_to_move.first_name + " " + person_to_move.second_name
        else:  # the person to move is not there
            print("The person you have entered is not in the system.")
            print("\n\n\t\t\t---------------------------\n\n")
            return "no_person"

        current_occupants_room_name = None
        new_room_type = None
        if isinstance(person_to_move, Staff):  # the person to move is a Staff
            string_to_return += ", staff"
            if isinstance(room_to_change_to, LivingSpace):
                print("A Staff cannot be moved to a living space room")
                print("\n\n\t\t\t---------------------------\n\n")
                return "staff_no_living_space"
            else:
                new_room_type = "Office: "
                current_occupants_room_name = person_to_move.office_name
                person_to_move.office_name = room_to_change_to.room_name  # assign a new office name to the person

                string_to_return += ", office"
        else:  # the person to move is a Fellow
            string_to_return += ", fellow"
            if isinstance(room_to_change_to, LivingSpace):
                new_room_type = "Living space: "
                current_occupants_room_name = person_to_move.livingspace_name
                person_to_move.livingspace_name = room_to_change_to.room_name  # assign a new living space to the person

                string_to_return += ", living space"
            else:
                new_room_type = "Office: "
                current_occupants_room_name = person_to_move.office_name
                person_to_move.office_name = room_to_change_to.room_name  # assign a new office space to the person

                string_to_return += ", office"

        if current_occupants_room_name is None:
            current_occupants_room_name = "unassigned"
        elif current_occupants_room_name == room_name:
            print("The person is already assigned to the room you want to reallocate to.")
            print("\n\n\t\t\t---------------------------\n\n")
            return "same_room"

        print(first_name + " " + second_name + " has been reallocated from " + new_room_type +
              current_occupants_room_name + " to: " + room_name)

        string_to_return += ", " + current_occupants_room_name

        # do the reallocating
        # loop through all rooms to get the previously occupied room and reduce its occupants
        old_room_to_free = None
        index_of_room = -1
        for old_room in self.all_rooms:
            index_of_room += 1
            if old_room.room_name == current_occupants_room_name:
                old_room_to_free = old_room
                break

        if old_room_to_free is not None:
            person_we_want_moved = None
            for person in self.all_rooms[index_of_room].occupants:
                person_name_moved = person.first_name + " " + person.second_name
                if person_name_moved == first_name + " " + second_name:
                    person_we_want_moved = person
                    break
            self.all_rooms[index_of_room].occupants.remove(person_we_want_moved)
            # del old_room_to_free.occupants[index_of_room]
            # print("length is", len(old_room_to_free.occupants))

        current_occupants = room_to_change_to.occupants
        current_occupants.append(person_to_move)

        return string_to_return

    def load_people(self, file_name):
        """
        Load people written in the text file provided into the system
        :param file_name:
        :return:
        """

        if len(file_name) < 4:
            return "short"
        elif file_name.split(".")[-1] != "txt":
            return "not txt file"

        try:
            with open(file_name, "r") as file_to_read:
                data = file_to_read.readlines()
                for line in data:
                    words = line.split()
                    if len(words) > 3:  # the command has 4 args
                        self.add_person(words[0],words[1], words[2], words[3])
                    else:  # the command has only 3 args, hence no accommodation
                        self.add_person(words[0], words[1], words[2])

            print('People loaded successfully from a text file')
            print("\n\n\t\t\t---------------------------\n\n")

        except IOError:
            print('Failed to write to the file provided')
            print("\n\n\t\t\t---------------------------\n\n")

        return file_name

    def save_state(self, sqlite_db=None):
        """
        Saves all the data currently in the program to an sqlite database provided.
        If no db is provided, a default database is used
        :param sqlite_db:
        :return:
        """

        if sqlite_db is None:
            db = Database()
        else:
            if len(sqlite_db) < 7:
                return "short"
            elif sqlite_db.split(".")[-1] != "sqlite":
                return "not sqlite file"
            else:
                db = Database(sqlite_db)

        db.clear_state()
        # loop through all the people in the list and save them in the sqlite database
        for person in self.all_people:
            db.add_person(person)

        # loop through all the rooms in the list and save them in the sqlite database
        for room in self.all_rooms:
            db.add_room(room)

        print('State of the application saved successfully')
        print("\n\n\t\t\t---------------------------\n\n")

        return sqlite_db

    def load_state(self, sqlite_db):
        """
        Loads data from a database into the application
        :param sqlite_db:
        :return:
        """

        # first clear the lists in the application to avoid duplication
        self.all_rooms.clear()
        self.all_people.clear()
        if len(sqlite_db) < 7:
            return "short"
        elif sqlite_db.split(".")[-1] != "sqlite":
            return "not sqlite file"
        else:
            db = Database(sqlite_db)
            self.all_people = db.get_people_list()
            self.all_rooms = db.get_rooms_list()

        print('Database information loaded into the application successfully')
        print("\n\n\t\t\t---------------------------\n\n")

        return sqlite_db
