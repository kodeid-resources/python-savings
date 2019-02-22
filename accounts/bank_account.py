class BankAccount:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!!!\n")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance
