def count_letters(sentence: str)-> dict:
    letters = dict()

    for letter in sentence:
        if letter in letters.keys():
            letters[letter] += 1
        elif letter.isalpha():
            letters[letter] = 1

    return letters


def main():
    
    sentence = input("Enter a sentence: ")
    
    letters = count_letters(sentence)

    for key, value in letters.items():
        print(f"{key}:{value}")


if __name__ == '__main__':
    main()
