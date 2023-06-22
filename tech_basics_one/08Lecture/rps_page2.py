# import the libraries that we will be working with
import tkinter as tk
import random


# create the graphical user interfacce
root = tk.Tk()
# give your gui a title
root.title('Rock Paper Scissor')
# create a new gui
root.geometry('650x450')
# change the colour
# root.configure(background='blue')

# create a message variable which will print the final message
message = tk.Label()
comp_selection = tk.Label()
user_score_label = tk.Label()
comp_score_label = tk.Label()
# keep track of scores
computer_score = 0
user_score = 0


def computer_selection():
    """This definition selects rock or paper or scissor at random"""
    options = ["Rock", "Paper", "Scissors"]
    comp_selection = random.choice(options)

    return comp_selection


def press(user_selects):
    global message, comp_selection, computer_score, user_score, user_score_label, comp_score_label

    message.destroy()  # We are forgetting or removing old label so that new text can come properly
    comp_selection.destroy()
    user_score_label.grid_forget()
    comp_score_label.grid_forget()

    computer_selects = computer_selection()

    comp_selection = tk.Label(text=f'The computer selects {computer_selects}', font='arial 15 bold', bg='Red', fg='Black')
    comp_selection.grid(row=9, column=0, pady=15)

    if user_selects == computer_selects:
        message = tk.Label(text=f'PLAYERS DRAW! PLEASE PLAY AGAIN', font='arial 15 bold', bg='Black', fg='Yellow')
    elif user_selects == "Rock" and computer_selects == "Scissors":
        message = tk.Label(text='PLAYER ONE WINS!! ROCK SMASHES PAPER', font='arial 15 bold', bg='Black', fg='Yellow')
        user_score += 1
    elif user_selects == "Scissors" and computer_selects == "Paper":
        message = tk.Label(text='PLAYER ONE WINS!! SCISSORS CUTS PAPER', font='arial 15 bold', bg='Black', fg='Yellow')
        user_score += 1
    elif user_selects == "Paper" and computer_selects == "Rock":
        message = tk.Label(text='PLAYER ONE WINS!! PAPER COVER ROCKS', font='arial 15 bold', bg='Black', fg='Yellow')
        user_score += 1
    else:
        message = tk.Label(text='THE COMPUTER WINS', font='arial 15 bold', bg='Black', fg='Yellow')
        computer_score += 1

    message.grid(row=10, column=0, pady=30)

    # add a label with the scores
    user_score_label = tk.Label(text=f"Player Score: {user_score}", bg='#4834DF', fg='#ffffff', borderwidth=5, relief=tk.RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    user_score_label.grid(row=13, column=0, pady=15)
    
    comp_score_label = tk.Label(text=f"PC Score: {computer_score}", bg='#4834DF', fg='white', borderwidth=5, relief=tk.RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    comp_score_label.grid(row=14, column=0, pady=15)


# Layout of RPS Game
# add buttons for player 1
welcome = tk.Label(text='Welcome to Rock vs Paper vs Scissors', font='arial 25 bold', bg='Pink', fg='Black')
# place on a grid
welcome.grid(columnspan=1, row=0, ipadx=70, padx=33, pady=10)
# add a label for player one
player_one = tk.Label(text=f'Good Luck Player One!!! Make your selection', font='Arial 16', fg='white')
player_one.grid(row=1, column=0, pady=15)

# add buttons the player can select
rock = tk.Button(text='Rock', font='arial 14 bold', height=1, width=7, command=lambda: press("Rock"))
rock.grid(row=3, column=0)
paper = tk.Button(text='Paper', font='arial 14 bold', height=1, width=7, command=lambda: press("Paper"))
paper.grid(row=4, column=0)
scissors = tk.Button(text='Scissors', font='arial 14 bold', height=1, width=7, command=lambda: press("Scissors"))
scissors.grid(row=5, column=0)

# add a close button which will close the game
exit_button = tk.Button(text='Close Game', command=root.destroy, font='arial 10 bold')
exit_button.place(x=500, y=410)


root.mainloop()