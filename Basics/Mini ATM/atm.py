from bank_account import BankAccount

class ATM:

    def __init__(self):

        __current_account = None

    def bank_account_on(self, account: BankAccount):
        self.__current_account = account

    def bank_account_off(self):
        self.__current_account = None

    def withdraw(self, quantity):

        assert self.__current_account, "No bank account!"
        assert quantity <= self.__current_account.balance, "Your balance is not sufficient!"
        assert quantity > 0, "Quantity must be positive!"

        self.__current_account.balance -= quantity
        return self.get_balance()

    def deposit(self, quantity):

        assert quantity > 0, "The quantity cannot be negative!"
        assert self.__current_account, "No bank account!"

        self.__current_account.balance += quantity
        return self.get_balance()
        
    def get_balance(self):
        
        assert self.__current_account, "No bank account!"

        return self.__current_account.balance


    def __repr__(self):
        return "ATM()"


