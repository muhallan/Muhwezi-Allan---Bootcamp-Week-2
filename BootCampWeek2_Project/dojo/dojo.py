"""Dojo Space Allocation

Adapted the docopt code from this documentation
    Credit: https://github.com/docopt/docopt/blob/master/examples/interactive_example.py

Usage:
    dojo.py create_room <room_type> <room_name>...
    dojo.py add_person <person_name> FELLOW|STAFF [wants_accommodation]
    dojo.py (-i | --interactive)
    dojo.py (-h | --help | --version)

    Options:
        -h,--help           : Show this help message and exit
        --version           : Show version.
        -i, --interactive   : Interactive Mode
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from room import Room

#Boilerplate code copied from the link mentioned above
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class Dojo(cmd.Cmd):
    """Dojo class which is the main class of the system. It calls and implements most of the
    functionality needed in the system"""

    intro = 'Welcome to my Dojo Space Allocation program!' \
        + ' (type help for a list of commands.)'
    prompt = '(Type your command) '
    file = None

    def __init__(self):
        self.all_rooms = []
        self.all_people = []

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""

        """Creates rooms in the Dojo.
            Creates a room after receiving as arguments the type of the room and its name.
            Multiple names can be passed and that would create as many rooms with those names"""
        
        # check if the arguments passed have a room type: room types are 'office' and 'living_space'
        if args['<room_type>'] == "office": #room type of 'office'
            if args['<room_name>'] != None:
                


        new_rooms = []
        for each_room_name in room_name:
            room = Room(room_type, each_room_name)
            new_rooms.append(room)

        self.all_rooms.extend(new_rooms)

    def add_person(self, person_name):
        """Adds a person to the system and allocates the person a random room"""
        pass

if __name__ == '__main__':
    #args = docopt(__doc__)
    args = docopt(__doc__, version='Dojo Space Allocation 1.0')
    #main(args)
    print(args)
