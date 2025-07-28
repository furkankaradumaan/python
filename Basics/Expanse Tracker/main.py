from enum import Enum
from expense import *
from income import *

class OPERATIONS(Enum):
    ADD_EXPENSE = 1
    ADD_INCOME = 2
    LIST = 3
    SUM_EXPENSE = 4
    SUM_INCOME = 5
    EXIT = 6

def show_menu():
    print("1-ADD EXPENSE")
    print("2-ADD INCOME")
    print("3-LIST")
    print("4-TOTAL EXPENSES")
    print("5-TOTAL INCOMES")
    print("6-EXIT")

def main():
    
    Expense.load_from_csv()
    Income.load_from_csv()

    while True:
        show_menu()
    
        try:
            command = int(input("Enter your choice: "))
        except ValueError as e:
            print(e)
            exit()

        match command:
        
            case OPERATIONS.ADD_EXPENSE.value:
                add_expense()
    
            case OPERATIONS.ADD_INCOME.value:
                add_income()
       
            case OPERATIONS.LIST.value:
                print("EXPENSES".center(16, '-'))
                Expense.list_expenses()
                print("INCOMES".center(16, '-'))
                Income.list_incomes()

            case OPERATIONS.SUM_EXPENSE.value:
                expenses = Expense.total_expenses()
                print("-" * 40)
                print(f"Total expenses: {expenses}.")
                print("-" * 40)
            case OPERATIONS.SUM_INCOME.value:
                incomes = Income.total_incomes()
                print("-" * 40)
                print(f"Total incomes: {incomes}.")
                print("-" * 40)
            case OPERATIONS.EXIT.value:
                Expense.save_to_csv()
                Income.save_to_csv()
                print("Terminating expanse tracker...")
                exit()
            case _:
                print("Invalid command!")
if __name__ == '__main__':
    main()
