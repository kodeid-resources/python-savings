from .bank_account import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(self, balance)
