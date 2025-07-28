from datetime import date
from enum import Enum
import csv

class CATEGORY(Enum):
    SALARY = 1
    RENT = 2
    DEBT = 3
    OTHER = 4

class Income:
    
    __incomes = []
    __csv_name = "incomes.csv"

    def __init__(self, iid: int, category, amount: float, edate = date.today()):

        assert amount > 0, "Amount must be greater than 0"

        self.id = iid
        self.category = category
        self.date = edate
        self.amount = amount

        self.__incomes.append(self)

    def __radd__(self, other):
        return self.amount + other

    @classmethod
    def load_from_csv(cls):
        with open(cls.__csv_name, "r") as file:
            
            reader = csv.DictReader(file)

            for row in reader:
                Income(row["id"], CATEGORY[row["category"][9:]], float(row["amount"]), date.fromisoformat(row["date"]))

    @classmethod
    def save_to_csv(cls):
        with open(cls.__csv_name, "w") as file:

            writer = csv.writer(file)

            writer.writerow(["id", "category", "amount", "date"])

            for income in cls.__incomes:
                writer.writerow([income.id, income.category, income.amount, income.date])

    @classmethod
    def total_incomes(cls):
        return sum(cls.__incomes)

    def __str__(self):
        return f"ID: {self.id}\nDate: {self.date}\nCATEGORY: {self.category.name}\nAMOUNT: {self.amount}"

    @classmethod
    def list_incomes(cls):
        for income in cls.__incomes:
            print("-" * 40)
            print(income)
            print("-" * 40)

def add_income():

    iid = None
    category: CATEGORY = None
    amount = None

    try:
        iid = int(input("Income ID: "))
        category = int(input("Category: "))
        amount = int(input("Amount: "))
    except ValueError as e:
        print(e)

    if not iid or not category or not amount:
        return -1
    if not 6 > category > 0:
        return -1

    Income(iid, CATEGORY(category), amount)
    return 1

