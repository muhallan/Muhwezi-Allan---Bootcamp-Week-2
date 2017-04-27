from person import Person

class Fellow(Person):
    """
    Fellow class that inherits from Person but includes data for accomodation
    """
    def __init__(self, fellow_name, office_name, wants_accommodation, livingspace_name=None):
        super(Fellow, self).__init__(fellow_name, office_name)
        self.__wants_accommodation = wants_accommodation
        self.__livingspace_name = livingspace_name

    @property
    def wants_accommodation(self):
        """
        Returns the boolean as of whether the Fellow wants accommodation or not
        :return: wants_accommodation
        """
        return self.__wants_accommodation
    
    @wants_accommodation.setter
    def wants_accommodation(self, wants_accommodation):
        """
        Setter for the wants_accommodation attribute
        :param wants_accommodation
        :return:
        """

    @property
    def livingspace_name(self):
        """
        Getter for livingspace_name attribute
        :return: livingspace_name
        """
        return self.__livingspace_name
    
    @livingspace_name.setter
    def livingspace_name(self, livingspace_name):
        """
        Setter for the livingspace_name attribute
        :param livingspace_name
        :return:
        """
