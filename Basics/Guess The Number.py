import random


LOWER = 1
UPPER = 20

print(f"I am thinking of a number between {LOWER} and {UPPER}")
number = random.randint(LOWER, UPPER)
guess = None

guesses = 0
while guess != number and guesses < 6:
    try:
        guess = int(input("Take a guess: "))

        guesses += 1
        if guess > number:
            print("Your guess is too high!")
        elif guess < number:
            print("Your guess is too low!")
    except ValueError as e:
        print(e)

if guess == number:
    print(f"Good job! You guessed my number in {guesses} guesses!")
else:
    print(f"Nope. The number I was thinking of was {number}")
