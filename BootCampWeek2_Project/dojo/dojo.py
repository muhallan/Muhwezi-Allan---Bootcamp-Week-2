""" Dojo Space Allocation
Usage:
    dojo.py create_room <room_type> <room_name>...
    dojo.py add_person <person_name> FELLOW|STAFF [wants_accommodation]

    Options:
        -h,--help       : Show this help message
        --version       : Show version.
"""
import cmd
from docopt import docopt

from room import Room


class Dojo(cmd.Cmd):
    """Dojo class which is the main class of the system. It calls and implements most of the
    functionality needed in the system"""

    def __init__(self):
        self.all_rooms = []
        self.all_people = []

    def create_room(self, room_type, *room_name):
        """Creates rooms in the Dojo.
            Creates a room after receiving as arguments the type of the room and its name.
            Multiple names can be passed and that would create as many rooms with those names"""

        new_rooms = []
        for each_room_name in room_name:
            room = Room(room_type, each_room_name)
            new_rooms.append(room)

        self.all_rooms.extend(new_rooms)

    def add_person(self, person_name):
        """Adds a person to the system and allocates the person a random room"""
        pass

    if __name__ == '__main__':
        args = docopt(__doc__)
        #arguments = docopt(__doc__, version='Dojo Space Allocation 1.0')
        #main(args)
        print(args)
