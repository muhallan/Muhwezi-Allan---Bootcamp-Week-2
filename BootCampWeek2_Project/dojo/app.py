"""Dojo Space Allocation

Usage:
    dojo.py create_room <room_type> <room_name>...
    dojo.py add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
    dojo.py print_room <room_name>
    dojo.py print_allocations [<-o=filename>]
    dojo.py print_unallocated [<-o=filename>]
    dojo.py (-i | --interactive)
    dojo.py (-h | --help | --version)

    Options:
        -h,--help           : Show this help message and exit
        --version           : Show version.
        -i, --interactive   : Interactive Mode
        quit                : Quit the interactive mode
        -o                  : filename
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

my_dojo = Dojo() #get the Dojo object to use to call its methods

class App(cmd.Cmd):
    """
    The App class ties everything together.
    It inherits from CMD and hence is used to get arguments and commands from the command line
    using docopt.
    The commands entered direct which methods to call from Dojo so as to carry out the tasks
    """

    intro = '\n\t\tWelcome to my Dojo Space Allocation program!' \
        + '\n\n\t\t\t----------------------\n' \
        + '\nCommands: \n\tcreate_room <room_type> <room_name>...' \
        + '\n\tadd_person <first_name> <last_name> <person_type> [<wants_accommodation>]' \
        + '\n\tprint_room <room_name>' \
        + '\n\tprint_allocations [-o=filename]' \
        + '\n\tprint_unallocated [-o=filename]' \
        + ' \n\n\t\t(type help for a list of commands.)\n\n'
    prompt = '(Type your command) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>...
        """

        # check if the arguments passed are of room types 'office' and 'livingspace'
        if args['<room_type>'].lower() == "office": #room type of 'office'
            if args['<room_name>'] != None:
                #store the entered room names in a list
                entered_room_names = args['<room_name>']

                for room_name in entered_room_names: # loop through the list getting each room name
                    my_dojo.create_room("office", room_name)

        elif args['<room_type>'].lower() == "livingspace":
            if args['<room_name>'] != None:
                #store the entered room names in a list
                entered_room_names = args['<room_name>']

                for room_name in entered_room_names: # loop through the list getting each room name
                    my_dojo.create_room("livingspace", room_name)
        else:
            print("Wrong first argument. Must be 'office' or 'livingspace'")
            print("\n\n\t\t\t---------------------------\n\n")

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> <person_type> [<wants_accommodation>]
        """

        first_name = args['<first_name>']
        second_name = args['<last_name>']

        if args['<person_type>'].lower() == "fellow": #add a person who is a Fellow

            if args['<wants_accommodation>'] == None: #the accommodation condition was not input. It's N by default
                my_dojo.add_person(first_name, second_name, "fellow")

            elif args['<wants_accommodation>'].lower() == "y": #the fellow wants an accommodation
                my_dojo.add_person(first_name, second_name, "fellow", "Y")

            elif args['<wants_accommodation>'].lower() == "n": #the fellow doesn't want an accommodation
                my_dojo.add_person(first_name, second_name, "fellow")
            else:
                print("Invalid argument for 'wants accommodation'. Must be 'Y' or 'N' or left empty")
                print("\n\n\t\t\t---------------------------\n\n")
        elif args['<person_type>'].lower() == "staff": #add a person who is a Staff

            if args['<wants_accommodation>'] != None: #the accommodation condition was input. Raise an error
                print("Staff are not provided with accommodation. Leave the last argument empty")
                print("\n\n\t\t\t---------------------------\n\n")
            else:
                my_dojo.add_person(first_name, second_name, "staff")
        else:
            print("Wrong argument for person type. Must be a 'fellow' or 'staff'")
            print("\n\n\t\t\t---------------------------\n\n")

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>
        """
        room_name = args['<room_name>']

        my_dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, args):
        """ Usage: print_allocations [<-o=filename>]
        """
        if args['<-o=filename>'] == None: #no args were input, hence no writing to file, just print
            my_dojo.print_allocations()
        else:
            filename = args['<-o=filename>']

            if len(filename) < 4: #short file name
                print("Invalid file name.")
            elif filename.split(".")[-1] != "txt": #must end with .txt
                print("Invalid file name.")
            else:
                my_dojo.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [<-o=filename>]
        """
        if args['<-o=filename>'] == None: #no args were input, hence no writing to file, just print
            my_dojo.print_unallocated()
        else:
            filename = args['<-o=filename>']

            if len(filename) < 4: #short file name
                print("Invalid file name.")
            elif filename.split(".")[-1] != "txt": #must end with .txt
                print("Invalid file name.")
            else:
                my_dojo.print_unallocated(filename)

    @docopt_cmd
    def do_quit(self, args):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

if __name__ == '__main__':
    opt = docopt(__doc__, sys.argv[1:], help=True)
    if opt['--interactive']:
        App().cmdloop()