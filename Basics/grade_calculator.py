def get_grade(prompt: str)-> float:
    
    """
    Get a floating point number in the
    interval [0, 100]. Keep asking until
    user enters a valid grade.
    """
    grade: float = None

    while True:
        try:
            grade = float(input(prompt))

            if not 100 >= grade >= 0:
                raise ValueError("Grade must be between 0 and 100 (both inclusive).")
            break
        except ValueError as error:
            print(error)
    
    return grade

def calculate_letter_grade(grade: float)-> str:

    if grade > 100:
        raise ValueError("Grade must be between 0 and 100 (both inclusive)")
    elif grade >= 90:
        return "AA"
    elif grade >= 80:
        return "BA"
    elif grade >= 70:
        return "BB"
    elif grade >= 60:
        return "CB"
    elif grade >= 50:
        return "CC"
    elif grade >= 40:
        return "DC"
    elif grade >= 0:
        return "FF"
    else:
        raise ValueError("Grade must be between 0 and 100 (both inclusive)")


def main():

    grade = get_grade("Enter your grade: ")

    try:
        letter_grade = calculate_letter_grade(grade)
    except ValueError as e:
        print(e)
    else:
        print(f"Your letter grade is {letter_grade}.")


if __name__ == "__main__":
    main()
