
from room import Room

class LivingSpace(Room):
    """
    LivingSpace class that inherits from the Room class and is used to create rooms for living in for fellows
    """

    def __init__(self, room_type, room_name):
        super(LivingSpace, self).__init__(room_type, room_name)
        self.room_type = "Living Space"
        self.room_name = room_name
        self.max_number_of_occupants = 4

    