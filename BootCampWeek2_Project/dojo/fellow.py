from person import Person


class Fellow(Person):
    """
    Fellow class that inherits from Person but includes data for accommodation
    """
    def __init__(self, first_name, second_name, wants_accommodation, office_name=None,
                 livingspace_name=None, is_allocated=False):
        super(Fellow, self).__init__(first_name, second_name, office_name, is_allocated)
        self.wants_accommodation = wants_accommodation
        self.livingspace_name = livingspace_name
