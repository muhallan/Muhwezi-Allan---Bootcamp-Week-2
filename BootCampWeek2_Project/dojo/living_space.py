
from room import Room

class LivingSpace(Room):
    """
    LivingSpace class that inherits from the Room class and is used to create rooms
    for living in for fellows
    """

    def __init__(self, room_name):
        super(LivingSpace, self).__init__("Living Space", room_name)
        self.max_number_of_occupants = 4

    