from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random

def generate_password(small_letters: int, big_letters: int,
                      ndigits: int, special: int):
    password = ""
    
    if small_letters:
        password += "".join(random.choices(ascii_lowercase, k=small_letters))

    if big_letters:
        password += "".join(random.choices(ascii_uppercase, k=big_letters))

    if ndigits:
        password += "".join(random.choices(digits, k=ndigits))
    
    if special:
        password += "".join(random.choices(punctuation, k=special))

    return password




def main():

    small_letters: int = None
    big_letters: int = None
    digits: int = None
    special: int = None

    try:
        small_letters = int(input("Number of small letters: "))
        big_letters = int(input("Number of big letters: "))
        digits = int(input("Number of digits: "))
        special = int(input("Number of special characters: "))
    except ValueError as e:
        print(e)
    else:
        password = generate_password(
                small_letters,
                big_letters,
                digits,
                special)

        print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
