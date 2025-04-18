from Client import Client
import client_data

class RegisteredClient(Client):
    """RegisteredClient is a subclass of Client."""

    def __init__(self, bank_account: str, first_name: str, last_name: str, middle_name: str = ""):
        """Registered client constructor"""
        self.client_id = self.set_client_id()
        self.completed_orders = []  # list of file names that contain completed orders
        self.pending_orders = []  # list of file names that contain pending orders
        super().__init__('EE' + bank_account, first_name, last_name, middle_name)

    def set_client_id(self):
        """Sets the current client's id by checking main programs inputs."""
        pass

    def get_client_id(self):
        """Returns client id."""
        return self.client_id

    def get_full_name(self) -> list:
        """
        Returns an ordered list containing the users first, middle and last name.
        """
        return [self.first_name, self.middle_name, self.last_name]

    def get_bank_account(self):
        """Returns the bank stored bank account."""
        return self.bank_account

    def set_bank_account(self):
        """Sets the bank account of the registered user."""
        pass

    def get_order(self, order_id):
        """Returns a specific order."""
        pass

    def get_all_orders(self) -> list:
        """Returns a list of pending and completed orders."""
        return self.completed_orders + self.pending_orders

    def get_completed_orders(self) -> list:
        """Returns a list of completed orders."""
        return self.completed_orders

    def get_pending_orders(self) -> list:
        """Returns a list of pending orders."""
        return self.pending_orders
