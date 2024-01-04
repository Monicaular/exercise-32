import random

def pick_random_word():
    """
    This function picks a random word from the SOWPODS
    dictionary. 
    """
    # open the sowpods dictionary
    with open("sowpods.txt", 'r') as f:
        words = f.readlines()

    # generate a random index
    # -1 because len(words) is not a valid index into the list `words`
    index = random.randint(0, len(words) - 1)

    # print out the word at that index
    word = words[index].strip()
    return word

def ask_user_for_next_letter():
    """
    This function prompts the user to input a letter,
    removes any leading or trailing whitespaces, converts it to uppercase,
    and returns the letter.
    """
    letter = input("Guess your letter: ")
    return letter.strip().upper()