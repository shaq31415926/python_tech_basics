# References:
# https://www.codegrepper.com/code-examples/python/python+hangman
# https://inventwithpython.com/invent4thed/chapter8.html

import random
import os

# definition that generates random word
def get_random_word(word_list):
    random_word = random.choice(word_list)

    return random_word


# definition that starts the game by clearing the screen, generating a random word and displaying the random word

def start_game(word_list):
    # code to clear screen
    os.system("clear")  # use cls if window machine. This clears the screen

    # generate secret word
    secret_word = get_random_word(word_list)

    # create a variable that prints dashes instead of secret word
    display_secret_word =  list("_"*len(secret_word))
    # you want to print this when the game begins
    print("Welcome to my Hangman Game")
    # this code takes all the items from the list and joins
    # useful code for us to create the secret word
    print(" ".join(display_secret_word))

    return secret_word, display_secret_word

# the list of hangman pics is how many chances you want to give the user
# you could copy the list from here if you don't want to create your own: https://github.com/shaq31415926/python_tech_basics/blob/014f5bc5f6b0743f960f25d6b348782073fe9fe9/tech_basics_one/09Lecture/hangman.py#L14C1-L56C14
# choice of hangman options
hangman_pics = ["""
    +---+
        |
        |
        |
       ===""",
     """
     +---+
     O   |
         |
         |
        ===""",
     """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
     """
    +---+
    O   |
   /|\  |
        |
       ===""",
   """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
  """
   +---+
   O   |
  /|\  |
  / \  |
      ==="""]


def play_hangman():
    # set parameters to start the game
    trials = 0
    max_trials = len(hangman_pics)
    display_hangman = ""  # if user guesses first letter correctly, display nothing
    guessed_letter_list = []  # list to keep track of letters guessed_word
    word_list = ["cat", "dog", "sweet"]


    # call the definition that will clear the screen and generate a secret word and display the secret word
    secret_word, display_secret_word = start_game(word_list)

    # you will keep looping through the game until the user has lost all turns
    while trials < max_trials:
        # ask the user to guess a letter
        guessed_letter = input("Guess a letter?:").lower().strip()

        if guessed_letter in guessed_letter_list:
            print("You already used this letter. Try another letter")

        # if user guesses letter correctly
        if guessed_letter in secret_word:
            print("That is correct")
            # replace the dashes with the letter
            for i in range(len(secret_word)):
                if list(secret_word)[i] == guessed_letter:
                    display_secret_word[i] = guessed_letter
            # if user guesses word correctly, exit the game
            if "".join(display_secret_word) == secret_word:
                os.system("clear")
                print(" ".join(display_secret_word))
                print("Congratulations!!!! You guessed the word correctly.")
                break

        # if the user guesses the letter incorrectly
        else:
            if max_trials - trials - 1 > 0:
                print(f"You have {max_trials - trials - 1} goes left")
            # create a variable that will display the hangman pic
            display_hangman = hangman_pics[trials]
            # add one to the trial variable to reduce the number of tries the user has
            trials += 1

        # what do we want to show the user when they lose
        if trials == max_trials:
            os.system("clear")
            print("-" * 50)
            print("Game over! You are dead :()")
            print(f"The correct word was {secret_word}")
            print(display_hangman)
            print("-" * 50)
        # what do we want to show the user each round
        else:
            print(" ".join(display_secret_word))  # you want to print that each round
            print(display_hangman)
            guessed_letter_list += [guessed_letter]  # keep track of guessed letters

play_hangman()