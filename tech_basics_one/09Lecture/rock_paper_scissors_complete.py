# import the libraries that we will be working with
import tkinter as tk
from PIL import Image, ImageTk
import random

# create the graphical user interfacce
root = tk.Tk()

# give your gui a title
root.title('Rock Paper Scissor')

# set the configuration of GUI window
root.geometry("650x450")

# Create the frame for the first windows of the game
f1 = tk.Frame(root)
# read the image you want to use for the first fra,e
img = Image.open('images/rps.jpeg')
# resize the image
img = img.resize((650, 450), Image.LANCZOS)
# add this code to view the image as the frame
pic = ImageTk.PhotoImage(img)
Lab = tk.Label(f1, image=pic)
Lab.pack()
f1.pack()

# add buttons to your first frame so the user can add their name
# Create some widgets and place them above the image

# print a message asking the user for their name
name = tk.Label(root, text='Please Enter Your Name :', font='arial 15 bold')
# where would you like to place this button
name.place(x=230, y=20)
# This variable will store the name of user
nameinp = tk.StringVar()

# create a message variable which will print the final message
message = tk.Label()
comp_selection = tk.Label()
L2 = tk.Label()
L3 = tk.Label()
# keep track of scores
pcscore = 0
userscore = 0


def computer_selection():
    # the computer selects rock or paper or scissor at random
    comp_selection = random.choice(['Rock', 'Paper', 'Scissors'])

    return comp_selection


def press(value):
    global message, comp_selection, pcscore, userscore, nameinp, L2, L3

    message.grid_forget()  # We are forgetting or removing old label so that new text can come properly
    comp_selection.destroy()
    L2.grid_forget()
    L3.grid_forget()

    # player_selection = tk.Label(text=f'You have selected {value}', font='arial 15', bg='Black', fg='White')
    # player_selection.grid(row=8, column=0, pady=15)

    computer = computer_selection()

    comp_selection = tk.Label(text=f'The computer selects {computer}', font='arial 15 bold', bg='Red', fg='Black')
    comp_selection.grid(row=9, column=0, pady=15)

    if value == computer:
        message = tk.Label(text=f'PLAYERS DRAW! PLEASE PLAY AGAIN', font='arial 15 bold', bg='Black', fg='Yellow')
    elif value == "Rock" and computer == "Scissors":
        message = tk.Label(text=f'{nameinp.get().upper()} WINS !! ROCK SMASHES PAPER', font='arial 15 bold', bg='Black', fg='Yellow')
        userscore += 1
    elif value == "Scissors" and computer == "Paper":
        message = tk.Label(text=f'{nameinp.get().upper()} WINS!! SCISSORS CUTS PAPER', font='arial 15 bold', bg='Black', fg='Yellow')
        userscore += 1
    elif value == "Paper" and computer == "Rock":
        message = tk.Label(text=f'{nameinp.get().upper()} ONE WINS!! PAPER COVER ROCKS', font='arial 15 bold', bg='Black', fg='Yellow')
        userscore += 1
    else:
        message = tk.Label(text='THE COMPUTER WINS', font='arial 15 bold', bg='Black', fg='Yellow')
        pcscore += 1

    message.grid(row=10, column=0, pady=30)

    # add a score
    L2 = tk.Label(text=f"Player Score: {userscore}", bg='#4834DF', fg='#ffffff', borderwidth=5, relief=tk.RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L2.grid(row=13, column=0, pady=15)
    L3 = tk.Label(text=f"PC Score: {pcscore}", bg='#4834DF', fg='white', borderwidth=5, relief=tk.RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L3.grid(row=14, column=0, pady=15)


def entergame(event):
    maingame()

def maingame():
    global nameinp

    # create a new gui
    root.geometry('650x450')
    # destroy all the variables we created for the first window
    name.destroy()
    f1.destroy()
    inpname.destroy()
    play_button.destroy()

    # Layout of RPS Game
    # add buttons for player 1 and player 2

    head = tk.Label(text='Welcome to Rock vs Paper vs Scissors', font='arial 25 bold', bg='Pink', fg='Black')
    # place on a grid
    head.grid(columnspan=1, row=0, ipadx=70, padx=33, pady=10)
    # add a label for player one
    player_one = tk.Label(text=f'Good Luck {nameinp.get().capitalize()}!!! Make your selection', font='Arial 16', fg='white')
    player_one.grid(row=1, column=0, pady=15)

    # add buttons the player can select
    rock = tk.Button(text='Rock', font='arial 14 bold', height=1, width=7, command=lambda: press("Rock"))
    rock.grid(row=3, column=0)
    paper = tk.Button(text='Paper', font='arial 14 bold', height=1, width=7, command=lambda: press("Paper"))
    paper.grid(row=4, column=0)
    scissors = tk.Button(text='Scissors', font='arial 14 bold', height=1, width=7, command=lambda: press("Scissors"))
    scissors.grid(row=5, column=0)

    # add a close button which will close the game
    btnclose = tk.Button(text='Close Game', command=root.destroy, font='arial 10 bold')
    btnclose.place(x=500, y=410)


# create an entry box to store the users name
inpname = tk.Entry(root, textvar=nameinp, font='arial 15 bold')
# We binded Return event with inpname entry widget i.e. if enter key is pressed then entergame function will be called
inpname.bind('<Return>',
             entergame)
inpname.place(x=230, y=60)

# add a let's play button

play_button = tk.Button(text="Let's Play", font='lucida 10 bold', command=maingame)
play_button.place(x=305, y=88)

root.mainloop()
