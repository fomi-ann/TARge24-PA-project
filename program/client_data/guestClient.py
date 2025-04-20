from Client import Client

class GuestClient(Client):
    """GuestClient is a subclass of Client"""

    def __init__(self, bank_account: str, first_name: str, last_name: str, middle_name: str = ""):
        """GuestClient constructor."""
        super().__init__(bank_account, first_name, last_name, middle_name)

    def get_full_name_list(self) -> list:
        """
        Returns an ordered list containing the users first, middle and last name.
        """
        return [self.first_name, self.middle_name, self.last_name]

    def get_full_name(self) -> str:
        """Returns the clients full name as a string."""
        return self.first_name + " " + self.middle_name + " " + self.last_name

    def get_bank_account(self):
        """Returns clients bank account."""
        return self.bank_account

    def __repr__(self):
        return f"Guest client. Name: {self.get_full_name()}. Bank account: {self.bank_account}"