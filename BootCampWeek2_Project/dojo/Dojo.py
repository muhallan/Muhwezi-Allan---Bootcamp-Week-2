import sys
import cmd
from docopt import docopt, DocoptExit

"""Dojo class"""
class Dojo(cmd.Cmd):
    def __init__(self, all_rooms):
        self.all_rooms = all_rooms
    def create_room(self, room_type, *room_name):
        for room in room_name:
            create()
        pass
    def add_person(self, person_name):
        pass