"""Dojo Space Allocation

Usage:
    dojo.py create_room <room_type> <room_name>...
    dojo.py add_person <person_name> FELLOW|STAFF [wants_accommodation]
    dojo.py (-i | --interactive)
    dojo.py (-h | --help | --version)

    Options:
        -h,--help           : Show this help message and exit
        --version           : Show version.
        -i, --interactive   : Interactive Mode
        quit                : Quit the interactive mode
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo import Dojo

"""
Adapted the docopt code from this documentation
    Credit: https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
"""

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

class App(cmd.Cmd):
    """
    The App class ties everything together.
    It inherits from CMD and hence is used to get arguments and commands from the command line
    using docopt.
    The commands entered direct which methods to call from Dojo so as to carry out the tasks
    """

    intro = '\n\tWelcome to my Dojo Space Allocation program!' \
        + ' \t\t\t\t(type help for a list of commands.)\n\n'
    prompt = '(Type your command) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""

        my_dojo = Dojo()

        # check if the arguments passed are of room types 'office' and 'livingspace'
        if args['<room_type>'] == "office": #room type of 'office'
            if args['<room_name>'] != None:
                #store the entered room names in a list
                entered_room_names = args['<room_name>']

                for room_name in entered_room_names: # loop through the list getting each room name
                    my_dojo.create_room("office", room_name)

        elif args['<room_type>'] == "livingspace":
            if args['<room_name>'] != None:
                #store the entered room names in a list
                entered_room_names = args['<room_name>']

                for room_name in entered_room_names: # loop through the list getting each room name
                    my_dojo.create_room("livingspace", room_name)
        else:
            print("Wrong first argument. Must be 'office' or 'livingspace'")

    @docopt_cmd
    def do_add_person(self, person_name):
        """Usage: add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        """
        pass

    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:], help=True)
    if opt['--interactive']:
        App().cmdloop()