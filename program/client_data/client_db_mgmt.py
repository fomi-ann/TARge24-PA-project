from Client import Client
from program.client_data.guestClient import GuestClient


def read_db():
    """Reads the existing database into a variable and returns it."""
    pass


def save_client_to_db(client: Client):
    """Saves client information to database"""
    pass


def remove_client_from_db(client_id):
    """Removes the registered client from the database."""
    pass


def init_client(user_data: list = None, user_id=None):
    """Creates a client subclass for the current program session."""
    if user_id is None and user_data is not None:
        # Guest client initiation
        guest_client = GuestClient(*user_data)
    elif user_id is not None and user_data is None:
        # Registered user initiation from database
        pass
    else:
        # 1. New registered user initiation
        # 2. save to database.
        pass


def create_client_id() -> str:
    """
    Creates a random string 8 characters long.
    1. Creates 8 random single digit numbers
    2. Adds them together as a string
    3. Checks if string is in registeredClients.csv
    4. If string is in file, runs the function again
    5. Returns the string if it is not in file
    """
    pass
