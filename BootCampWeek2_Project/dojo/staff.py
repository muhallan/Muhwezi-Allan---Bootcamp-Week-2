from person import Person

class Staff(Person):
    """
    Staff class that inherits from the Person. Used to create people who are staff.
    """
    def __init__(self, first_name, second_name, office_name=None, is_allocated=False):
        super(Staff, self).__init__(first_name, second_name, office_name, is_allocated)
        