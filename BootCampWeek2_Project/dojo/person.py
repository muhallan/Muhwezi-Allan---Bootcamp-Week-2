
class Person(object):
    """
    The Person class that provides a superclass for Fellow and Staff subclasses
    """
    def __init__(self, person_name, office_name):
        """
        The init method of Person. Every person created is expected to have a name and an office
        """
        self.__person_name = person_name
        self.__office_name = office_name

    @property
    def person_name(self):
        """
        This is a getter for the person_name attribute.
        :return: person_name
        """
        return self.__person_name

    @person_name.setter
    def person_name(self, person_name):
        """
        Setter for the person_name attribute
        :param person_name 
        :return: 
        """

    @property
    def office_name(self):
        """
        Getter for the office_name attribute
        :return: office_name
        """
        return self.__office_name

    @office_name.setter
    def office_name(self, office_name):
        """
        Setter of the office_name attrbute
        :param office_name
        :return:
        """
