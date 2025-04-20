from Client import Client


def read_db():
    """Reads the existing database into a variable and returns it."""
    pass

def save_client_to_db(client:Client):
    """Saves client information to database"""
    pass

def remove_client_from_db(client_id):
    """Removes the registered client from the database."""
    pass

def init_client(user_id):
    """Creates a registered client subclass for the current program session."""
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