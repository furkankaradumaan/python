def collatz(number):
    if number % 2 == 0:
        return number // 2
    return number * 3 + 1


try:
    number = int(input("Enter a number: "))
except ValueError as e:
    print(e)
else:
    while number != 1:
        number = collatz(number)
        print(number)

        
