from abc import ABC, abstractmethod


class Client(ABC):

    def __init__(self, bank_account: str, first_name: str, last_name: str, middle_name: str = ""):
        """Client constructor."""
        self.bank_account = "EE" + bank_account  # EE{however many numbers a bank account has}
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    @abstractmethod
    def get_bank_account(self):
        """
        Get bank account method which every subclass overrides.
        """
        pass

    @abstractmethod
    def get_full_name(self) -> list:
        """
        Get full name method which every subclass overrides.
        """
        pass
