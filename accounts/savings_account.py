from .bank_account import BankAccount


class SavingsAccount(BankAccount):
    def transfer(self, account, amount):
        if amount <= account.get_balance():
            account.withdraw(amount)
            self.deposit(amount)
            print("Transfered Rp. {} into your savings account\n".format(amount))
        else:
            print("Insufficient funds!!!\n")
