# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that you have the rules down, you can start thinking about how they might translate to Python code.
# --------

# This version of the code, asks if the player wants to play again only if they draw
while True:
    # Take the user input - two users enters their choice
    player_1_selection = input("Player 1 - Enter a choice (rock, paper, scissors): ")
    player_1_selection  = player_1_selection.lower() # lowercase the input

    player_2_selection = input("Player 2 - Enter a choice (rock, paper, scissors): ")
    player_2_selection  = player_2_selection.lower() # lowercase the input

    ## do not do next part without testing the first part

    # if the players drawer
    if  player_1_selection == player_2_selection:
        print("The players draw")
        play_again = input("Would you like to play again? Y/N:")
        if play_again.lower() != "y":
            print("Thank you for playing!")
            break
    # otherwise, depending on player selection define which player wins or loses
    else:
        if player_1_selection == "rock":
            if player_2_selection == "rock":
                print("The players draw")
            elif player_2_selection == "paper":
                print("The second player wins")
            else:
                print("The first player wins")
        elif player_1_selection == "paper":
            if player_2_selection == "paper":
                print("The players draw")
            elif player_2_selection == "scissors":
                print("The second player wins")
            else:
                print("The first player wins")
        elif player_1_selection == "scissors":
            if player_2_selection == "scissors":
                print("The players draw")
            elif player_2_selection == "rock":
                print("The second player wins")
            else:
                print("The first player wins")
        break
