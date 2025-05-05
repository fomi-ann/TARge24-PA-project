from abc import ABC, abstractmethod


class Client(ABC):

    def __init__(self, first_name: str, last_name: str):
        """Client constructor."""
        #self.bank_account = bank_account
        self.first_name = first_name
        #self.middle_name = middle_name
        self.last_name = last_name

    # @abstractmethod
    # def get_bank_account(self):
    #     """
    #     Get bank account method which every subclass overrides.
    #     """
    #     pass
    #
    # @abstractmethod
    # def get_full_name_list(self) -> list:
    #     """
    #     Get full name list method which every subclass overrides.
    #     """
    #     pass
    # @abstractmethod
    # def get_full_name(self) -> str:
    #     """
    #     Get full name method which every subclass overrides.
    #     """
    #     pass