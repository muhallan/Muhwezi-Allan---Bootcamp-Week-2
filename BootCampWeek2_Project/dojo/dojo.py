""" Dojo Space Allocation
Usage:
    create_room <room_type> <room_name> - Creates rooms in the Dojo
    add_person <person_name> <FELLOW|STAFF> [wants_accommodation] - Adds a person to the system and allocates the person to a random room.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from room.room import Room

"""Dojo class which is the main class of the system. It calls and implements most of the
functionality needed in the system"""


class Dojo(cmd.Cmd):

    def __init__(self):
        self.all_rooms = []
        self.all_people = []

    def create_room(self, room_type, *room_name):
        """Creates rooms in the Dojo. creates a room after receiving as arguments the type of the room and its name.
            Multiple names can be passed and that would create as many rooms with those names"""

        room = Room()
        for room in room_name:
            """create()"""
        pass

    def add_person(self, person_name):
        """Adds a person to the system and allocates the person a random room"""
        pass
