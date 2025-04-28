import uuid

class Client:
    client_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())
        """Random generated ID"""
        Client.client_counter += 1