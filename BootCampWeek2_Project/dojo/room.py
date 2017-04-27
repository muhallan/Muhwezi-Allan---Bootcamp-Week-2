
class Room(object):
    """
    A Room class that is used to create a room in the Dojo.
    This is the super class that is inherited by OfficeSpace and LivingSpace classes
    """
    def __init__(self, room_type, room_name):
        """
        This is the initializer of the class. room_name and room_type as passed in while
        initializing Room objects
        """
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = [] #number of occupants currently in the room
