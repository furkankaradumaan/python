from enum import Enum
import csv
from datetime import date

class CATEGORY(Enum):
    FOOD = 1
    TEXTILE = 2
    FUN = 3
    RENT = 4
    CAR = 5
    OTHER = 6

class Expense:
    
    __expenses = []
    __csv_name = "expenses.csv"

    def __init__(self, eid: int, category: CATEGORY, amount: float, edate: date = date.today()):
        
        assert amount > 0, "Amount must be greater than 0"

        self.eid = eid
        self.category = category
        self.amount = amount
        self.date = edate

        Expense.__expenses.append(self)

    def __str__(self):
        return f"ID: {self.eid}\nDate: {self.date}\nCATEGORY: {self.category.name}\nAMOUNT: {self.amount}"
    @classmethod
    def total_expenses(cls):
        return sum(cls.__expenses)

    def __radd__(self, other):
        return self.amount + other

    @classmethod
    def load_from_csv(cls):
        with open(cls.__csv_name, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                Expense(row["id"], CATEGORY[row["category"][9:]], float(row["amount"]), date.fromisoformat(row["date"]))

    @classmethod
    def save_to_csv(cls):
        with open(cls.__csv_name, "w", newline="") as file:
            fieldnames = ["id", "category", "amount", "date"]
            writer = csv.writer(file)

            writer.writerow(fieldnames)
            for expense in cls.__expenses:
                writer.writerow([expense.eid, expense.category, expense.amount, expense.date])

    @classmethod
    def list_expenses(cls):
        for expense in cls.__expenses:
            print("-" * 40)
            print(expense)
            print("-" * 40)





def add_expense():

    eid = None
    category: CATEGORY = None
    amount = None

    try:
        eid = int(input("Expense ID: "))
        category = int(input("Category: "))
        amount = int(input("Amount: "))
    except ValueError as e:
        print(e)

    if not eid or not category or not amount:
        return -1
    if not 6 > category > 0:
        return -1

    Expense(eid, CATEGORY(category), amount)
    return 1



