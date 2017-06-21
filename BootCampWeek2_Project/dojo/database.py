import sqlite3

from staff import Staff
from fellow import Fellow
from living_space import LivingSpace
from office_space import OfficeSpace


class Database(object):
    """
    The Database helper class that is used to manage SQLite databases used in the system
    """
    def __init__(self, sqlite_filename=None):
        """
        This is the initializer of the Database class. It receives an optional SQLite db name.
        If it's not given a default one is used
        :param sqlite_filename:
        """
        if sqlite_filename is not None:
            self.sqlite_filename = sqlite_filename
        else:
            self.sqlite_filename = "sqlite_db.sqlite"

        # connecting to the database file
        self.conn = sqlite3.connect(self.sqlite_filename)
        self.c = self.conn.cursor()

        # creating a person table
        self.c.execute('''CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT,
                       second_name TEXT, person_type TEXT, accommodation INTEGER DEFAULT 0, office_name TEXT NULL,
                       living_space_name TEXT NULL, is_allocated INTEGER DEFAULT 0)''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS room (id INTEGER PRIMARY KEY AUTOINCREMENT, room_type TEXT,
                       room_name TEXT)''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS occupants (id INTEGER PRIMARY KEY AUTOINCREMENT, room_id INTEGER,
                       person_id INTEGER)''')

        self.conn.commit()

    def close(self):
        """
        Close the connection to the database
        :return:
        """
        self.conn.close()

    def add_person(self, person):
        """
        Add a person object of type Person to the person table. Person can either be Fellow or Staff
        :param person:
        :return:
        """
        allocation = 0
        person_type = ""
        if person.is_allocated:
            allocation = 1
        if isinstance(person, Staff):
            person_type = "staff"
            self.c.execute("""INSERT INTO person (first_name, second_name, person_type, office_name, is_allocated) VALUES (?, ?, ?, ?, ?)""",
            (person.first_name, person.second_name, person_type, person.office_name, allocation))
        else:
            accommodation = 0
            living_space = ""
            person_type = "fellow"
            if person.wants_accommodation:
                accommodation = 1
                living_space = person.livingspace_name
            self.c.execute("""INSERT INTO person (first_name, second_name, person_type, accommodation, office_name, living_space_name, is_allocated) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (person.first_name, person.second_name, person_type, accommodation, person.office_name, living_space, allocation))

        self.conn.commit()

    def add_occupant(self, room_id, person_id):
        """
        Add an occupant whose id is person_id of a room with id, room_id
        :param room_id:
        :param person_id:
        :return:
        """
        self.c.execute("INSERT INTO occupants (room_id, person_id) VALUES (?, ?)", (room_id, person_id))
        self.conn.commit()

    def add_room(self, room):
        """
        Add a room of type Room to the room table.
        :param room:
        :return:
        """
        self.c.execute("INSERT INTO room (room_type, room_name) VALUES (?, ?)", (room.room_type, room.room_name))

        last_id = self.c.lastrowid

        # get the id of each room occupant in the person table
        for person in room.occupants:
            self.c.execute("SELECT id FROM person WHERE first_name =? AND second_name =?",
                         (person.first_name, person.second_name))
            id_got = self.c.fetchone()[0]
            self.add_occupant(last_id, id_got)

        self.conn.commit()

    def clear_state(self):
        """
        Delete all the database tables before saving there data afresh
        :return:
        """
        self.c.execute("DELETE FROM person")
        self.c.execute("DELETE FROM room")
        self.c.execute("DELETE FROM occupants")
        self.conn.commit()

    def get_people_list(self, people_ids=None):
        """
        Queries the database's person table and puts the contents into the a List of type Person
        :param: people_ids: a list of ids of people that are occupants of a given room. this is optional
        :return: List of type Person
        """
        if people_ids is None:  # carry out a select on person table
            self.c.execute("SELECT * FROM person")
        else:
            format_string_ids = ','.join(['?'] * len(people_ids))
            self.c.execute("SELECT * FROM person WHERE id IN (%s)" % format_string_ids, tuple(people_ids))

        rows = self.c.fetchall()
        people = []
        for row in rows:
            first_name = row[1]
            second_name = row[2]
            person_type = row[3]
            accommodation = row[4]
            office_name = row[5]
            living_space = row[6]
            is_allocated = row[7]

            if is_allocated == 1:
                allocation = True
            else:
                allocation = False

            if person_type == "staff":  # this is a Staff
                staff = Staff(first_name, second_name, office_name, allocation)
                people.append(staff)
            else:  # this is a Fellow
                if accommodation == 0:
                    wants_accommodation = False
                else:
                    wants_accommodation = True

                if living_space == "" or living_space is None:
                    living_space_name = None
                else:
                    living_space_name = living_space

                fellow = Fellow(first_name, second_name, wants_accommodation, office_name, living_space_name, allocation)
                people.append(fellow)

        self.conn.commit()
        return people

    def get_rooms_list(self):
        """
        Query the room and occupants tables and fetch the rooms and their occupants into a list of type Room
        :return: List of type Room
        """
        self.c.execute("SELECT * FROM room")
        rows = self.c.fetchall()
        rooms = []
        for row in rows:
            id_ = row[0]
            room_type = row[1]
            room_name = row[2]

            occupants_cursor = self.conn.cursor()
            occupants_cursor.execute("SELECT person_id FROM occupants WHERE room_id = ?", (id_,))
            rows_occupants = occupants_cursor.fetchall()
            list_of_person_ids = []
            for p_id in rows_occupants:
                one_person_id = p_id[0]
                list_of_person_ids.append(one_person_id)

            # call the get_people_list method and pass it the list of ids
            room_occupants = self.get_people_list(list_of_person_ids)

            if room_type == "Living Space":  # LivingSpace room
                room = LivingSpace(room_name)
            else:
                room = OfficeSpace(room_name)

            room.occupants = room_occupants
            rooms.append(room)

        return rooms
