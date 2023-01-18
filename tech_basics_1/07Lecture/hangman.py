# reference:
# https://www.codegrepper.com/code-examples/python/python+hangman
# https://inventwithpython.com/invent4thed/chapter8.html

import random
import os

os.system("clear") # use cls if window machine. This clears the screen
print("Hello! This is the word for you to guess")

# list of words we want the user to guess
word_list = ["ant", "jaw", "ink", "chance", "sweet"]

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

display_hangman = ""

# get random word from list
def get_random_word(word_list):
    random_word = random.choice(word_list)

    return random_word

# select a word randomly for user to guess from the list
secret_word = get_random_word(word_list)

# display randomy chosen word in dash
# the guessed word is same length as number of dashes
guessed_word = list("_"*len(secret_word))
print(' '.join(guessed_word)) # formats the dashes to include a space

# how many chances does the user get_random_word
trials = 0
max_trials = len(hangman_pics)
guessed_letter_list = [] # list to keep track of letters guessed_word

while trials < max_trials:
    # ask the user for input
    guessed_letter = input("Guess a letter?:")
    guessed_letter = guessed_letter.lower().strip()

    # make sure the user only adds one letter at a time
    if len(guessed_letter) != 1:
        print("Please select one letter")
    elif guessed_letter in guessed_letter_list:
        print("You already used this letter. Try another letter")
    else:
        if guessed_letter in secret_word:
            print("That is correct")
            # identify if the letters in secret word match the user input
            for i in range(len(secret_word)):
                if list(secret_word)[i] == guessed_letter:
                    guessed_word[i] = guessed_letter
            # create a variables for guessed word
            if "".join(guessed_word) == secret_word:
                print(" ".join(guessed_word))
                print("Congratulations!!!! You guessed the word")
                break
        else:
            print(f"!!!!Keep guessing!!!!! You have {max_trials - trials - 1} goes left")
            # print from the list
            display_hangman = hangman_pics[trials]
            trials += 1


        if trials == max_trials:
            print("Game over! You are dead :()")
            print(f"The correct word was {secret_word}")
            print(display_hangman)
        else:
            # print the word and hagman after every round
            print(display_hangman)
            print(" ".join(guessed_word))
            guessed_letter_list += [guessed_letter] # keep track of guessed letters
