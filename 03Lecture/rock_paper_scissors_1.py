# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# Now that you have the rules down, you can start thinking about how they might translate to Python code.
# --------
while True:
    # Take the user input - two users enters their choice
    player_1_selection = input("Player 1 - Enter a choice (rock, paper, scissors): ")
    player_1_selection  = player_1_selection.lower() # lowercase the input

    player_2_selection = input("Player 2 - Enter a choice (rock, paper, scissors): ")
    player_2_selection  = player_2_selection.lower() # lowercase the input

    if player_1_selection == player_2_selection: # if a tie happens, this also removes lots of options
         print(f"Both players selected {player_1_selection}. It's a tie!")
         # if ties ask the user if they want to play again
         # ask the players if they want to play again
         play_again = input("Would you like to play again? Y/N:")
         if play_again.lower() == "n":
             print("I am going to close the game now")
             break
    elif player_1_selection == "rock": # if user selects rock
        if player_2_selection == "scissors": # if computer selects scissors, then computer wins
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_1_selection == "paper": # if user selects paper
        if player_2_selection == "rock": # if computer selects rocks, then computer wins
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_1_selection == "scissors": # if user select scissors
        if player_2_selection == "paper": # if computer selects rocks, then computer wins
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    break # add break so we do not loop through once we have won the game
    print("-"*50)
