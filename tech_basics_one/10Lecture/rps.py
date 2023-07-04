import tkinter as tk
from PIL import Image, ImageTk
import random

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Rock Paper Scissors")

# code to configure the size
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

# print a message asking the user for their name
name_label = tk.Label(root, text='Please Enter Your Name :', font='arial 15 bold')
# where would you like to place this button
name_label.place(x=230, y=20)

# create an entry box to store the users name
name = tk.StringVar() # This variable will store the name of user
name_box = tk.Entry(root, textvar=name, font='arial 15 bold')
name_box.place(x=230, y=60)

# create some variables to initialise our labels
message = tk.Label()
comp_select_label = tk.Label()

# create some variables to keep track of the score
user_score = 0
comp_score = 0

def computer_selection():
    """This function makes a random selection"""
    options = ["ROCK", "PAPER", "SCISSORS"]
    computer_selection = random.choice(options)

    return computer_selection


def press(user_selects):
    """This function defines what happens when the user selects an option"""
    global message, comp_select_label, comp_score, user_score, name

    # clear the labels each time we click on the button
    message.destroy()
    comp_select_label.destroy()

    comp_select = computer_selection()
    comp_select_label = tk.Label(text=f"The Computer Selects {comp_select}")
    comp_select_label.grid(row=9, column=0, pady=30)

    if user_selects == comp_select:
        message = tk.Label(text=f"The computer and {name.get()}  draw. Play again!!!")
    elif user_selects == "ROCK" and comp_select == "SCISSORS":
        message = tk.Label(text=f"ROCK SMASHES SCISSORS!!! {name.get().upper()} WINS")
        user_score += 1
        # user_score = user_score + 1
    elif user_selects == "SCISSORS" and comp_select == "PAPER":
        message = tk.Label(text=f"SCISSORS CUTS PAPER!!! {name.get().upper()} WINS")
        user_score += 1
    elif user_selects == "PAPER" and comp_select == "ROCK":
        message = tk.Label(text=f"PAPER COVER ROCK!!! {name.get().upper()} WINS")
        user_score += 1
    else:
        message = tk.Label(text="COMPUTER WINS")
        comp_score += 1

    message.grid(row=10, column=0, pady=15)

    # add labels to show the score
    user_score_label = tk.Label(text=f"Player Score: {user_score}",
                                relief=tk.RAISED,
                                bg='#4834DF',
                                fg='#ffffff',
                                borderwidth=5
                                )
    user_score_label.grid(row=13, column=0, pady=15)

    comp_score_label = tk.Label(text=f"Computer Score: {comp_score}",
                                relief=tk.RAISED,
                                bg='#4834DF',
                                fg='#ffffff',
                                borderwidth=5
                                )
    comp_score_label.grid(row=14, column=0)

def maingame():
    # destroy everything we created in the first gui window
    play_button.destroy()
    f1.destroy()
    name_box.destroy()
    name_label.destroy()

    # add labels and buttons you created for page 2
    # designing the layout of our second page
    welcome = tk.Label(text="Welcome to Rock vs Paper vs Scissors",
                       font="arial 20 bold",
                       bg="Pink",
                       fg="Blue"
                       )
    welcome.grid(row=0, columnspan=1, ipadx=70, padx=33, pady=10)

    second_message = tk.Label(text=f"Good luck {name.get().capitalize()}!! Please make your selection",
                              font="arial 15 bold",
                              bg="White",
                              fg="Blue"
                              )
    second_message.grid(row=1, column=0, pady=15)

    # add some buttons the player can select
    rock = tk.Button(text="ROCK",
                     font="arial 14 bold",
                     height=1,
                     width=7,
                     command=lambda: press("ROCK")
                     )
    rock.grid(row=3, column=0)

    paper = tk.Button(text="PAPER",
                      font="arial 14 bold",
                      height=1,
                      width=7,
                      command=lambda: press("PAPER")
                      )
    paper.grid(row=4, column=0)

    scissors = tk.Button(text="SCISSOR",
                         font="arial 14 bold",
                         height=1,
                         width=7,
                         command=lambda: press("SCISSOR")
                         )
    scissors.grid(row=5, column=0)

    # THE FINAL BUTTON WHICH CLOSES THE GAME
    exit_button = tk.Button(text="Close the Game",
                            command=root.destroy
                            )
    exit_button.place(x=500, y=410)

# create a box
play_button = tk.Button(
              text="LET'S PLAY",
              font="lucida 10 bold",
              command=maingame
)
play_button.place(x=305, y=88)


# code to execute the code
root.mainloop()


