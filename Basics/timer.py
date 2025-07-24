import time

"""
Basic timer program. Takes some quantity of
seconds from the user and counts until it seconds
becomes zero.
"""

def get_seconds(prompt: str)-> int:
    seconds = None
    while not seconds:

        try:
            seconds = int(input(prompt))
        except ValueError as e:
            print(e)
        else:
            return seconds
    
    return 


def main():

    seconds = get_seconds("Seconds: ")

    while seconds > 0:
        print(f"Seconds left: {seconds:02}")
        time.sleep(1)

        seconds -= 1
    
    print("Timer has ended.")

if __name__ == "__main__":
    main()
