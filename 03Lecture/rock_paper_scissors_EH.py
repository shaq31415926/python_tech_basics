# Super cool code by Eldrik that errors if you enter an incorrect option


player_1_selection = input("Player 1 - Enter a choice (rock, paper, scissors): ")
player_1_selection = player_1_selection.lower() #lowercase the input


while player_1_selection != "rock" and player_1_selection != "paper" and player_1_selection != "scissors":
   print("non valid input")
   player_1_selection = input("PLEASE ENTER VALID OPTION:")



player_2_selection = input("Player 2 - Enter a choice (rock, paper, scissors):")
player_2_selection = player_2_selection.lower() #lowercase the input

while player_2_selection != "rock" and player_2_selection != "paper" and player_2_selection != "scissors":
   print("non valid input")
   player_2_selection = input("PLEASE ENTER VALID OPTION:")


if player_1_selection == "rock":
   if player_2_selection == "rock":
       print("Draw")
   elif player_2_selection == "paper":
       print("Player 2 wins")
   else:
       print("Player 1 wins")

if player_1_selection == "paper":
   if player_2_selection == "paper":
       print("Draw")
   elif player_2_selection == "scissor":
       print("Player 2 wins")
   else:
       print("Player 1 wins")

if player_1_selection == "scissor":
   if player_2_selection == "scissor":
       print("Draw")
   elif player_2_selection == "rock":
       print("Player 2 wins")
   else:
       print("Player 1 wins")
