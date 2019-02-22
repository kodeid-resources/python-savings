from accounts.savings_account import SavingsAccount
from accounts.checking_account import CheckingAccount


def main():
    # Setup accounts
    savings_account = SavingsAccount(100000)
    checking_account = CheckingAccount(500000)

    # Check balance
    print('Savings account balance: Rp. ', savings_account.get_balance())
    print('Checking account balance: Rp. {}\n'.format(checking_account.get_balance()))

    # Transfer
    savings_account.transfer(checking_account, 100000)

    # Check balance
    print('Savings account balance: Rp. ', savings_account.get_balance())
    print('Checking account balance: Rp. {}\n'.format(checking_account.get_balance()))

main()
