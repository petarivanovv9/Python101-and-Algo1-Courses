from bank_account import BankAccount
import unittest


class TestBankAccount(unittest .TestCase):

    def setUp(self):
        self.my_bank_account = BankAccount("Rado", 1000, "$")

    def test_create_new_bank_account_class(self):
        self.assertTrue(isinstance(self.my_bank_account, BankAccount))

    # testvame dali tazi funkciq vrushta greshka
    def test_deposit_amount(self):
        with self.assertRaises(ValueError):
            self.my_bank_account.deposit(-1)
        self.my_bank_account.deposit(1000)
        self.assertEqual(self.my_bank_account.initial_balance, 2000)

    def test_check_balance(self):
        current_balance = self.my_bank_account.balance()

        self.assertEqual(self.my_bank_account.initial_balance, current_balance)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.my_bank_account.withdraw(-50)
        self.my_bank_account.withdraw(1000)
        self.assertEqual(self.my_bank_account.initial_balance, 0)

    def test_transfer_to(self):
        other_acc = BankAccount("Pesho", 1010, "$")
        # self.assertEqual(self.my_bank_account.currency, other_acc.currency)
        self.my_bank_account.transfer_to(other_acc, 500)
        self.assertEqual(self.my_bank_account.initial_balance, 1000-500)
        self.assertEqual(other_acc.initial_balance, 1010+500)

        result = self.my_bank_account.transfer_to(other_acc, 20)
        self.assertTrue(result)

    def test_transfer_negative_amount(self):
        other_acc = BankAccount("Pesho", 1010, "$")
        some_acc = BankAccount("Anton", 1000, "lqlq")

        with self.assertRaises(ValueError):
            self.my_bank_account.transfer_to(other_acc, -50)
            self.my_bank_account.transfer_to(other_acc, 1010)
            self.my_bank_account.transfer_to(some_acc, 40)

if __name__ == '__main__':
    unittest.main()
