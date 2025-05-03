import uuid

class Client:
    client_counter = 0

    def __init__(self, first_name: str, last_name: str):
        """Initialize client with first name and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = str(uuid.uuid4())
        """Random generated ID"""
        Client.client_counter += 1

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.id}'

