""" Dojo Space Allocation

Usage:
    create_room <room_type> <room_name> - Creates rooms in the Dojo
    add_person <person_name> <FELLOW|STAFF> [wants_accommodation] - Adds a person to the system and allocates the person to a random room.
    print_room <room_name> - Prints  the names of all the people in room_name on the screen.
    print_allocations [-o=filename] - Prints a list of allocations onto the screen
    print_unallocated [-o=filename] - Prints a list of unallocated people to the screen
    reallocate_person <person_identifier> <new_room_name> - Reallocate the person with person_identifier to new_room_name.
    load_people - Adds people to rooms from a txt file.
    save_state [--db=sqlite_database] - Persists all the data stored in the app to a SQLite database
    load_state <sqlite_database> - Loads data from a database into the application.
"""

import sys
import cmd
import sqlite3
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


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Dojo Space Allocator v 1.0")
    print(arguments)
