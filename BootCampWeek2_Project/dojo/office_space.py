from room import Room

class OfficeSpace(Room):
    """OfficeSpace  class that inherits from Room and is used to create office spaces
    for both Fellows and Staff
    """
    def __init__(self, room_type, room_name):
        super(OfficeSpace, self).__init__(room_type, room_name)
        self.room_type = "Office Space"
        self.room_name = room_name
        self.max_num_of_occupants = 6
