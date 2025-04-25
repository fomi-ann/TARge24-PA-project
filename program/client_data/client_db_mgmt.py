import random

from Client import Client
from program.client_data.guestClient import GuestClient

client_db = None


def read_db():
    """
    Reads the existing database into a variable.
    Returns nothing.
    Should be used at the start of a program.
    """
    pass


def save_client_to_db(client: Client):
    """Saves client information to database"""
    pass


def remove_client_from_db(client_id):
    """Removes the registered client from the database."""
    pass


def init_client(user_data: list = None, user_id=None):
    """Creates a client subclass for the current program session and returns it.
    1. If the method recieves only a list of values, it initiates a guest client class.
    2. If it recieves only the user_id then it initialises the user from the database.
    3. If it recieves both, it initialises a new registered user for the session.
    """
    ### HAS TO RETURN THE CLIENT CLASS VALUES ###
    if user_id is None and user_data is not None:
        # Guest client initiation
        guest_client = GuestClient(*user_data)
    elif user_id is not None and user_data is None:
        # Registered user initiation from database
        pass
    else:
        # 1. New registered user initiation
        # 2. save to database
        # 3. print user_id for user
        pass


def create_client_id() -> str:
    """
    Creates a random string 8 characters long.
    1. Creates 8 random single digit numbers
    2. Adds them together as a string
    3. Checks if string is in registeredClients.csv(database is loaded at the start of the program)
    4. If string is in file, runs the function again
    5. Returns the string if it is not in file
    """
    new_id = ""
    for x in range(0, 8):
        new_id += str(random.randint(0, 9))

    if new_id in client_db:
        new_id = create_client_id()
        return new_id
    else:
        return new_id
