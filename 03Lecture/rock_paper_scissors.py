# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that you have the rules down, you can start thinking about how they might translate to Python code.
# --------

# Take the user input - two users enters their choice
player_1_selection = input("Player 1 - Enter a choice (rock, paper, scissors): ")
player_1_selection  = player_1_selection.lower() # lowercase the input

player_2_selection = input("Player 2 - Enter a choice (rock, paper, scissors): ")
player_2_selection  = player_1_selection.lower() # lowercase the input


# v1 of the if else statement
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
elif player_1_selection == selection:
    if player_2_selection == selection:
        print("The players draw")
    elif player_2_selection == "rock":
        print("The second player wins")
    else:
        print("The first player wins")
