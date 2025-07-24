from atm import ATM
from bank_account import BankAccount

def get_command(prompt: str)-> str:
    return input(prompt)


def get_quantity(prompt: str)-> float:

    quantity = None
    
    while True:
        try:
            quantity = float(input(prompt))

        except ValueError:
            print("Enter a valid number!")
        else:
            return quantity

def main():

    atm = ATM()
    account = BankAccount("Furkan", "Karaduman", 0)
    atm.bank_account_on(account)

    command = None
    
    print("---WELCOME TO ATM---")

    while command != "quit":

        command = get_command("Your command: ")
        match command:

            case "deposit":
                quantity = get_quantity("Quantity: ")
                try:
                    atm.deposit(quantity)
                except AssertionError as e:
                    print(e)

            case "withdraw":
                quantity = get_quantity("Quantity: ")
                try:
                    atm.withdraw(quantity)
                except AssertionError as e:
                    print(e)
            case "balance":
                print(f"Balance: {atm.get_balance()}")
            
            case "quit":
                print("ATM program is terminating...")

if __name__ == '__main__':
    main()
