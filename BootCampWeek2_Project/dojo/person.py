
class Person(object):
    """
    The Person class that provides a superclass for Fellow and Staff subclasses
    """
    def __init__(self, first_name, second_name, office_name = None, is_allocated=False):
        """
        The init method of Person. Every person created is expected to have a name
        """
        self.first_name = first_name
        self.second_name = second_name
        self.is_allocated = is_allocated #refers to the fact that a person is allocated to an office and if it's a fellow and he wants a living space, he is allocated to one
        self.office_name = office_name
