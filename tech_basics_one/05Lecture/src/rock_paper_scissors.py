import os

# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that you have the rules down, you can start thinking about how they might translate to Python code.
# --------

os.system("clear")
round_number = 1

# This version of the code, asks if the player wants to play again only if they draw
while True:
    print(f"Welcome to round number {round_number} of Rock Paper Scissors")
    # Take the user input - two users enters their choice
    player_1_selection = input("Player 1 - Enter a choice (rock, paper, scissors): ")
    player_1_selection = player_1_selection.lower()  # lowercase the input

    player_2_selection = input("Player 2 - Enter a choice (rock, paper, scissors): ")
    player_2_selection = player_2_selection.lower()  # lowercase the input

    # do not do next part without testing the first part

    # if the players drawer
    if player_1_selection == player_2_selection:
        print("The players draw")
        play_again = input("Would you like to play again? Y/N:")
        round_number += 1

        if play_again.lower() == "n":
            print("Thank you for playing!")
            break
    # otherwise, depending on player selection define which player wins or loses
    else:
        if player_1_selection == "rock":
            if player_2_selection == "paper":
                print("Paper covers rock - The computer wins")
            elif player_2_selection == "scissors":
                print("Rock smashes scissors - You win")
            else:
                print("Error - option does not exist")

        elif player_1_selection == "paper":
            if player_2_selection == "scissors":
                print("Scissor cuts paper - The computer wins")
            elif player_2_selection == "rock":
                print("Paper cover rocks - You win")
            else:
                print("Error - option does not exist")
        elif player_1_selection == "scissors":
            if player_2_selection == "rock":
                print("Rock smashes scissors - The computer wins")
            elif player_2_selection == "paper":
                print("Scissor cuts paper - You win")
            else:
                print("Error - option does not exist")
        print("Thank you for playing!")
        break
