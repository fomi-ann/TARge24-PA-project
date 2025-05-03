from program.client_data.Client import Client
import client_data


class RegisteredClient(Client):
    """RegisteredClient is a subclass of Client."""

    def __init__(self, bank_account: str, first_name: str, last_name: str, middle_name: str = ""):
        """Registered client constructor"""
        self.id = None
        self.completed_orders = []  # list of file names that contain completed orders
        self.pending_orders = []  # list of file names that contain pending orders
        super().__init__(bank_account, first_name, last_name, middle_name)

    def get_client_data(self):
        """Creates a list of values corresponding to the database format."""
        return [self.id, self.get_full_name(), self.bank_account, str(self.completed_orders), str(self.pending_orders)]

    def set_client_id(self, user_id):
        """Sets the current client's id by checking main programs inputs."""
        self.id = user_id

    def init_orders(self, comp_orders:list, pen_orders:list):
        """Initialises orders from database data."""
        self.completed_orders = comp_orders
        self.pending_orders = pen_orders

    def get_client_id(self):
        """Returns client id."""
        return self.id

    def get_full_name_list(self) -> list:
        """
        Returns an ordered list containing the users first, middle and last name.
        """
        return [self.first_name, self.middle_name, self.last_name]

    def get_full_name(self) -> str:
        """Returns the clients full name as a string."""
        if self.middle_name == "":
            return self.first_name + " " + self.last_name
        return self.first_name + " " + self.middle_name + " " + self.last_name

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

    def __repr__(self):
        return f"ID:{self.id} BankAccount: {self.bank_account} Name:{self.get_full_name()} Completed orders = {self.completed_orders} Pending orders={self.pending_orders}"
