from person import Person

class Staff(Person):
    """
    Staff class that inherits from the Person. Used to create people who are staff.
    """
    def __init__(self, staff_name):
        super(Staff, self).__init__(staff_name)