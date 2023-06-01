import os

# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that Player 1 have the rules down, Player 1 can start thinking about how they might translate to Python code.
# --------

os.system("clear")
round_number = 1

# This version of the code, asks if the player wants to play again only if they draw
while True:
    print(f"Welcome to round number {round_number} of Rock Paper Scissors")
    player_1_name = input("What is your name Player 1?:")
    player_2_name = input("What is your name Player 2?:")
    
    # Take the user input - two users enters their choice
    player_1_selection = input(f"Player {player_1_name} - Enter a choice (rock, paper, scissors): ")
    player_1_selection = player_1_selection.lower()  # lowercase the input

    player_2_selection = input(f"Player {player_2_name} - Enter a choice (rock, paper, scissors): ")
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
                print("Paper covers rock - Player 2 wins")
            elif player_2_selection == "scissors":
                print("Rock smashes scissors - Player 1 wins")
            else:
                print("Error - option does not exist")

        elif player_1_selection == "paper":
            if player_2_selection == "scissors":
                print("Scissor cuts paper - Player 2 wins")
            elif player_2_selection == "rock":
                print("Paper cover rocks - Player 1 wins")
            else:
                print("Error - option does not exist")
        elif player_1_selection == "scissors":
            if player_2_selection == "rock":
                print("Rock smashes scissors - Player 2 wins")
            elif player_2_selection == "paper":
                print("Scissor cuts paper - Player 1 wins")
            else:
                print("Error - option does not exist")
        print("Thank Player 1 for playing!")
        break
