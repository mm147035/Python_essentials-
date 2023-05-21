import unittest
import bank_account


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = bank_account.BankAccount("123456789", "John Smith", 1000)

    """"This unit test checks whether the deposit method of the BankAccount class correctly adds the given amount to the balance of the account.
    It does this by creating an instance of the BankAccount class with an initial balance of 1000, and then calling the deposit method on this instance with an amount of 500. The test then checks whether the balance of the account is equal to 1500.
    If the deposit method is implemented correctly, this test should pass.
    """
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    """This unit test checks whether the withdraw method of the BankAccount class correctly subtracts the given amount from the balance of the account.
    It does this by creating an instance of the BankAccount class with an initial balance of 1000, and then calling the withdraw method on this instance with an amount of 200. The test then checks whether the balance of the account is equal to 800.
    If the withdraw method is implemented correctly, this test should pass.
    """
    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    """This unit test checks whether the withdraw method of the BankAccount class correctly handles cases where the withdrawal amount is greater than the current balance of the account.
    It does this by creating an instance of the BankAccount class with an initial balance of 1000, and then calling the withdraw method on this instance with an amount of 1500 (which is greater than the current balance). The test then checks whether the balance of the account remains at 1000 (i.e., the balance should not change in this case).
    If the withdraw method is implemented correctly and correctly handles cases of insufficient balance, this test should pass.
    """
    def test_insufficient_balance(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.balance, 1000)



if __name__ == '__main__':
    unittest.main()
