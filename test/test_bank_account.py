import unittest
from src.bank_account import BankAccount
from src.exceptions import InsufficientFundsError,WithdrawalTimeRestrictionError
from unittest.mock import patch
import os


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.acount=BankAccount(balance=1000, log_file="transaction_log.txt")
        self.target_account = BankAccount(balance=500)
    
    def tearDown(self):
        if os.path.exists(self.acount.log_file):
            os.remove(self.acount.log_file)

    def _count_lines(self,filename):
        with open (filename, "r") as f:
            return len(f.readlines())
            
    def test_deposit(self):
        new_balance=self.acount.deposit(500)
        # assert new_balance==1500
        self.assertEqual(new_balance,1500,'El Balance no es igual')

    def test_withdraw(self):
        new_balance=self.acount.withdraw(200)
        self.assertEqual(new_balance,800,'El Balance no es igual')

    def test_get_balance(self):
        self.assertEqual(self.acount.get_balance(),1000)

    def test_transaction_log(self):
        self.acount.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))
    
    def test_count_transactions(self):
        assert  self._count_lines(self.acount.log_file)== 1
        self.acount.deposit(500)
        assert  self._count_lines(self.acount.log_file)== 2

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.acount.withdraw(2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hour(self,mock_datetime):
        mock_datetime.now.return_value.hour= 10
        new_balance=self.acount.withdraw(100)
        self.assertEqual(new_balance,900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.acount.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.acount.withdraw(100)

    def test_deposit_varios_amounts(self):
        test_case=[{"ammount":100,"expected":1100},
                   {"ammount":3000,"expected":4000},
                   {"ammount":4500,"expected":5500}
                   ]
        for case in test_case:
            with self.subTest(case=test_case):
                self.acount=BankAccount(balance=1000,log_file="transaction.txt")
                new_balance= self.acount.deposit(case["ammount"])
                self.assertEqual(new_balance,case["expected"])