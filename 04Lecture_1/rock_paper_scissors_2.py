# This script is to build a single game to play rock paper scisscors against the computer
# Resource: https://realpython.com/python-rock-paper-scissors/

import random # we can use this module to simulate the computerÄs choices

# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that you have the rules down, you can start thinking about how they might translate to Python code.
# --------

# Take the user input - the user enters their choice

while True: # we add while to create a loop so we can play indefinitely
    user_action = input("Enter a choice (rock, paper, scissors): ")
    user_action  = user_action.lower() # lowercase the input

    # Make the choice for the computer. We use random.choice() to randomly select for the computer.
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    print("-"*50)
    # run this script! You should have the users choice and the computer choice.

    # Determine a winner, using an if..elif.. else block to compare player's choie and determine a winner.
    # lets write this else if statement out together
    if user_action == computer_action: # if a tie happens, this also removes lots of options
         print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock": # if user selects rock
        if computer_action == "scissors": # if computer selects scissors, then computer wins
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper": # if user selects paper
        if computer_action == "rock": # if computer selects rocks, then computer wins
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors": # if user select scissors
        if computer_action == "paper": # if computer selects rocks, then computer wins
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    print("-"*50)

    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        break
