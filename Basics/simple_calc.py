"""
This is a simple calculator program.

The program takes two numbers and a mathematical
operator from the keyboard. It evaluates the given
mathematical expression and prints its value. It
keeps until the user enters a invalid number or operator or
the keyword 'quit'
"""

def get_operator(prompt: str):
    operator : str = None
    
    while not operator or operator not in ["+", "-", "*", "/", "quit"]:
        operator = input(prompt)
    
    return operator

def get_number(prompt: str):
    number: float = None
    
    while True:
        try:
            number = float(input(prompt))
            break;
        except ValueError:
            print("You entered an invalid number! Try again.\n")
    
    return number

def evaluate(operator, number1, number2):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            if number1 == 0 and number2 == 0:
                raise ArithmeticError
            return number1 * number2
        case '/':
            return number1 / number2
        case _:
            raise ValueError("Invalid operator!")


# main function.
def main():
    
    operator: str = None
    number1 : float = None
    number2 : float = None
    looping : bool = True 
    result : float = None
    
    """
    We need to keep looping until the user enters the keyword 'quit'.
    If the user does, then the variable 'looping' will become False and
    the loop will be ended.
    """
    while looping:
        # Get inputs from user.
        operator = get_operator(prompt = "Enter the operator(or enter quit): ")
        if operator == "quit":
            print("Terminating the program...")
            looping = False
        else:
            number1 = get_number(prompt = "Enter the first number: ")
            number2 = get_number(prompt = "Enter the second number: ")
        
            try:
                result = evaluate(operator, number1, number2)
            except ZeroDivisionError:
                print("Error: division by zero!")
            except ValueError:
                print("Invalid operator!")
            except ArithmeticError:
                print("Invalid multiplication 0*0!")
            else:
                print(f"{number1} {operator} {number2} = {result}\n")

                    

if __name__ == "__main__":
    main()

