# Muhwezi-Allan---Bootcamp-Week-2 Project
## Introduction
### **Problem Description**
When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. In this exercise you will be required to digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

## Features
### **The system has the following constraints**
* The Dojo has rooms which can be living spaces or office spaces
* An office can accommodate a maximum of 6 people
* A living space can accommodate a maximum of 4 people
* A person to be allocated can be a fellow or staff
* Staff cannot be allocated living spaces
* Fellows have a choice to choose a living space or not
* This system allocates space to people at random automatically

### **The system has the following functionalities**
* A command line interface using `docopt`that has the following commands
    * `create_room <room_type> <room_name>` - Creates rooms in the Dojo
    * `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]` - Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either **Y** or **N**. The default value if it is not provided is **N**.
* `print_room <room_name>` function - Prints  the names of all the people in room_name on the screen. 
* `print_allocations [-o=filename]` function - Prints a list of allocations onto the screen. Specifying the optional `-o option` here outputs the registered allocations to a txt file.
* `print_unallocated [-o=filename]` function - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.
* `reallocate_person <person_identifier> <new_room_name>` function - Reallocate the person with person_identifier to new_room_name.
* `load_people` - Adds people to rooms from a txt file. See Appendix 1A for text input format.
* `save_state [--db=sqlite_database]` function - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified. 
* `load_state <sqlite_database>` function - Loads data from a database into the application.

## Dependencies
These are the Python modules that the project uses
* appdirs==1.4.3
* docopt==0.6.2
* nose==1.3.7
* packaging==16.8
* pyparsing==2.2.0
* six==1.10.0
