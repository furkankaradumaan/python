from datetime import datetime


def get_year(prompt: str)-> int:
    """
    We want to get a year from this year to 150 years back.
    While user input is invalid, the function will prompt the
    error message and will ask again and again for a valid year.
    """
    year: int = None # Initially none
    MAX_YEAR = datetime.now().year

    while True:
        try:
            year = int(input(prompt))
    
            if year < MAX_YEAR - 150 or year > MAX_YEAR:
                raise ValueError(f"year must be between {MAX_YEAR - 150} and {MAX_YEAR}.")
            break
        except ValueError as e:
            print(e)
    
    return year

"""
Given a year as input.
Calculate the years from the current year and return
the result.
"""
def calculate_age(year: int)-> int:
    return datetime.now().year - year


def main():
    
    year = get_year("Enter a year: ")
    age = calculate_age(year)

    print(f"Your age is {age}.")


if __name__ == "__main__":
    main()
