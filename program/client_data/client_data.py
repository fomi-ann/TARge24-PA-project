from Client import Client

def save_client(client:Client):
    """Saves client information to registeredClients.csv"""
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