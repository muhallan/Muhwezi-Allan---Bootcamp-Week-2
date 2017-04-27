
class Person(object):
    """
    The Person class that provides a superclass for Fellow and Staff subclasses
    """
    def __init__(self, first_name, second_name, is_allocated=False):
        """
        The init method of Person. Every person created is expected to have a name
        """
        self.__first_name = first_name
        self.__second_name = second_name
        self.__is_allocated = is_allocated #refers to the fact that a person is allocated to an office and if it's a fellow and he wants a living space, he is allocated to one
        self.__office_name = None

    @property
    def first_name(self):
        """
        This is a getter for the first_name attribute.
        :return: first_name
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Setter for the first_name attribute
        :param first_name
        :return:
        """

    @property
    def second_name(self):
        """
        This is a getter for the second_name attribute.
        :return: second_name
        """
        return self.__second_name

    @second_name.setter
    def second_name(self, second_name):
        """
        Setter for the second_name attribute
        :param second_name
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
    @property
    def is_allocated(self):
        """
        Getter for the is_allocated attribute
        :return: is_allocated
        """
        return self.__is_allocated

    @is_allocated.setter
    def is_allocated(self, is_allocated):
        """
        Setter of the is_allocated attrbute
        :param is_allocated
        :return:
        """
