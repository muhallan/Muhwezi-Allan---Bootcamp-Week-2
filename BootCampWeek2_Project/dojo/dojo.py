""" Dojo Space Allocation
Usage:
    dojo.py create_room <room_type> <room_name>...
    dojo.py add_person <person_name> <FELLOW|STAFF> [wants_accommodation]

    Options:
        -h,--help       : Show this help message
        --version       : Show version.
        required        : example of a required argument
        repeating       : example of repeating arguments
        -f,--flag       : example flag #1
        -g,--greatflag  : example of flag #2
        -o,--otherflag  : example of flag #3
"""

import cmd

from docopt import docopt

from room import Room

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

    def main(self, docopt_args):
        """ main-entry point for program, expects dict with arguments from docopt() """
        # User passed the required argument
        if docopt_args["<required>"]:
            print("You have used the required argument: " + docopt_args["<required>"])

            # Get flags used
            if docopt_args["--flag"]:
                print("   with --flag\n")
            elif docopt_args["--greatflag"]:
                print("   with --greatflag\n")
            elif docopt_args["--otherflag"]:
                print("   with --otherflag\n")
            else:
                print("   with no flags.\n")
        # User passed 1 or more repeating arguments
        elif docopt_args["<repeating>"]:
            print("You have used the repeating args:")
            print('   ' + '\n   '.join(docopt_args["<repeating>"]) + '\n')

    if __name__ == '__main__':
        args = docopt(__doc__)
        #arguments = docopt(__doc__, version='Dojo Space Allocation 1.0')
        main(args)
