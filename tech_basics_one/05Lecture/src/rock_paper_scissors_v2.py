import os
import random

# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that you have the rules down, you can start thinking about how they might translate to Python code.
# --------

os.system("clear")

print(f"Welcome to Rock Paper Scissors")
# Take the user input - two users enters their choice
user_name = input("What is your name?:")
user_selection = input(f"Hi {user_name}, enter a choice (rock, paper, scissors): ")
user_selection = user_selection.lower()  # lowercase the input

choices = ["rock", "paper", "scissors"]
computer_selection = random.choice(choices)
print(f"The computer selected {computer_selection}")

# do not do next part without testing the first part

# if the players drawer
if user_selection == computer_selection:
    print("The players draw")
else:
    if user_selection == "rock":
        if computer_selection == "paper":
            print("Paper covers rock - The computer wins")
        elif computer_selection == "scissors":
            print("Rock smashes scissors - You win")
        else:
            print("Error - option does not exist")

    elif user_selection == "paper":
        if computer_selection == "scissors":
            print("Scissor cuts paper - The computer wins")
        elif computer_selection == "rock":
            print("Paper cover rocks - You win")
        else:
            print("Error - option does not exist")
    elif user_selection == "scissors":
        if computer_selection == "rock":
            print("Rock smashes scissors - The computer wins")
        elif computer_selection == "paper":
            print("Scissor cuts paper - You win")
        else:
            print("Error - option does not exist")

print("Thank you for playing!")