# This program defines a class for a BankAccount and simulates transactions.

class BankAccount:

    """__init__: This function is the constructor for the BankAccount class.
     It takes in three arguments: account_number, account_holder, and balance,
     and initializes the object's properties with these values.
    """
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    """deposit: This function allows you to deposit money into the BankAccount object.
     It takes in one argument, amount, which is the amount of money to be deposited.
     It updates the balance property of the BankAccount object and prints a message to the console showing the deposited amount and the new balance.
    """

    def deposit(self, amount):
        self.balance += amount
        print("Deposited $", amount, ". New balance: $", self.balance, sep='')

    """withdraw: This function allows you to withdraw money from the BankAccount object, if there is enough balance available.
     It takes in one argument, amount, which is the amount of money to be withdrawn. If there is not enough balance, it prints an error message to the console.
     Otherwise, it updates the balance property of the BankAccount object and prints a message to the console showing the withdrawn amount and the new balance.
    """

    def withdraw(self, amount):
        if self.balance < amount:
            print("Error: Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrew $", amount, ". New balance: $", self.balance, sep='')

# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Smith", 1000)

# Deposit and withdraw money from the account
account.deposit(500)
account.withdraw(100)
account.withdraw(1400)

# Print the account's number, holder, and balance
print("Account Number:", account.account_number)
print("Account Holder:", account.account_holder)
print("Balance:", account.balance)
