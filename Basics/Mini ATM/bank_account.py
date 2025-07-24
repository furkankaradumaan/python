class BankAccount:

    def __init__(self, name, lastname, balance):

        self.__name = name
        self.__lastname = lastname
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):

        assert balance >= 0, "Balance cannot be negative!"

        self.__balance = balance

    def __repr__(self):
        return f'BankAccount({self.name} {self.lastname} {self.balance})'


