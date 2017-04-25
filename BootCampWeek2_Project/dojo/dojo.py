""" Dojo Space Allocation
Usage:
    create_room <room_type> <room_name> - Creates rooms in the Dojo
    add_person <person_name> <FELLOW|STAFF> [wants_accommodation] - Adds a person to the system and allocates the person to a random room.
"""

import sys
import cmd
from docopt import docopt, DocoptExit

"""Dojo class"""


class Dojo(cmd.Cmd):

    def __init__(self):
        self.all_rooms = []
        self.all_people = []

    def create_room(self, room_type, *room_name):
        for room in room_name:
            """create()"""
        pass

    def add_person(self, person_name):
        pass