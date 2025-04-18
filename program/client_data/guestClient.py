from Client import Client

class GuestClient(Client):
    """GuestClient is a subclass of Client"""

    def __init__(self, bank_account: str, first_name: str, last_name: str, middle_name: str = ""):
        """GuestClient constructor."""
        super().__init__(bank_account, first_name, last_name, middle_name)

    def get_full_name(self) -> list:
        """
        Returns an ordered list containing the users first, middle and last name.
        """
        return [self.first_name, self.middle_name, self.last_name]

    def get_bank_account(self):
        """Returns clients bank account."""
        return self.bank_account