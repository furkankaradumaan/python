import unittest
from atm import ATM
from bank_account import BankAccount

class TestATM(unittest.TestCase):
    
    def setUp(self):
        
        self.acc1 = BankAccount("Furkan", "Karaduman", 0)
        self.acc2 = BankAccount("Betül", "Karaduman", 1000)
        self.atm = ATM()
    

    def test_withdraw(self):
        self.atm.bank_account_on(self.acc2)
        
        self.assertEqual(self.atm.withdraw(150), 850)
        self.assertRaises(AssertionError, self.atm.withdraw, -120)
        self.assertEqual(self.atm.withdraw(400), 450)
        self.assertEqual(self.atm.withdraw(450), 0)
        self.assertRaises(AssertionError, self.atm.withdraw, 100)
        
        self.atm.bank_account_off()
        self.assertRaises(AssertionError, self.atm.withdraw, 150)

    def test_deposit(self):

        self.atm.bank_account_on(self.acc1)

        self.assertEqual(self.atm.deposit(120), 120)
        self.assertEqual(self.atm.deposit(400), 520)
        self.assertRaises(AssertionError, self.atm.deposit, -200)
        
        self.atm.bank_account_off()

        self.atm.bank_account_on(self.acc2)

        self.assertEqual(self.atm.deposit(200), 1200)

    def test_get_balance(self):

        self.atm.bank_account_on(self.acc2)

        self.assertEqual(self.atm.get_balance(), 1000)
        
        self.atm.bank_account_off()

        self.assertRaises(AssertionError, self.atm.get_balance)


if __name__ == '__main__':
    unittest.main()
