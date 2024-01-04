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

def generate_word_string(word, letters_guessed):
    """
    This function takes a word and a set of letters guessed.
    It creates a string where guessed letters are shown, and unguessed letters are represented by underscores.
    The resulting string is returned.
    """
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)