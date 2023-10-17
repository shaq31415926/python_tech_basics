# References:
# https://www.codegrepper.com/code-examples/python/python+hangman
# https://inventwithpython.com/invent4thed/chapter8.html

import os
import random

# clear the terminal
os.system("clear") # window users use cls instead clear
print("Welcome to my Hangman Game. Prepare to die")


def display_secret_word(word_list):
    # select a word at random
    secret_word = random.choice(word_list)

    # show dashes in place of the secret word and store these dashes as a list
    display_word = list("-"*len(secret_word))
    print(" ".join(display_word))

    return secret_word, display_word


# create a list that contain some words
word_list = ["bat", "cat", "sweet", "zebra"]
secret_word, display_word = display_secret_word(word_list)

# create a list that contains the hangman images you want to show each time the user is incorrect
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

# create some parameters
trial = 0
max_trial = len(hangman_pics)
display_hangman = ""

# ask the user for a letter
while trial < max_trial:
    guessed_letter = input("Guess a letter:")

    # if the user guesses the letter correctly, do something
    if guessed_letter in secret_word:
        print("You guessed correctly")
        # replace the dashes with the letter
        for i in range(len(secret_word)):
            if list(secret_word)[i] == guessed_letter:
                display_word[i] = guessed_letter
        # if user guesses word correctly
        if "".join(display_word) == secret_word:
            print("Congratulations!! You guessed the word :)")
            break

    # if they did not guess correctly
    else:
        display_hangman = hangman_pics[trial]
        trial += 1

    # if the user reaches max trials
    if trial == max_trial:
        print(display_hangman)
        print("Game over, you are dead")
    else:
        print(f"Keep going. You have {max_trial - trial} goes left")
        print(display_hangman)
        print(" ".join(display_word))