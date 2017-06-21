from room import Room


class OfficeSpace(Room):
    """OfficeSpace  class that inherits from Room and is used to create office spaces
    for both Fellows and Staff
    """
    def __init__(self, room_name):
        super(OfficeSpace, self).__init__("Office Space", room_name)
        self.max_num_of_occupants = 6
