import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import messagebox


def display_secret_word(word_list):
    # select a word at random
    secret_word = random.choice(word_list)

    # show dashes in place of the secret word and store these dashes as a list
    display_word = list("-" * len(secret_word))

    return secret_word, display_word


# create a list that contain some words
word_list = ["bat", "cat", "sweet", "zebra"]
secret_word, display_word = display_secret_word(word_list)

# create gui window
root = tk.Tk()
# give your gui a title
root.title("Hangman")
# set the size of the gui
root.minsize(width=450, height=450)
# change colour of background
root.configure(background="black")

# create label that welcomes the user
title = tk.Label(root,
                 text="Guess the Letter",
                 fg="red",
                 font="Geneva 30 bold"
                 )
title.place(x=100, y=0)

# create a box where user can enter the letter
guessed_letter = tk.StringVar()
letter_entry = tk.Entry(root,
                        textvariable=guessed_letter,
                        fg="white",
                        font="Geneva 25 bold"
                        )
letter_entry.place(x=50, y=350)

# create a label that will display the dashes
display = tk.Label(root,
                   text=display_word,
                   fg="white",
                   font="Geneva 40 bold")
display.place(x=140, y=50)


def check_length(guessed_letter):
    if len(guessed_letter) > 1:
        tk.messagebox.showwarning("Warning", "Please enter only one letter")


def create_hangman_pic(trial):
    global new_image, canvas

    # Create a canvas
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    canvas.place(x=100, y=120)
    # Load an image in the script
    img = Image.open(f"images/{trial}.png")

    # Resize the Image using resize method
    resized_image = img.resize((200, 200), Image.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_image)

    # Add image to the Canvas Items
    canvas.create_image(60, 100, anchor=tk.CENTER, image=new_image)


trial = 0


def play_hangman():
    global guessed_letter, secret_word, display, display_word, title, letter_entry, play_button, trial

    # alert pops up if user enters more than one letter
    check_length(guessed_letter.get().lower())

    # if the user guesses the letter correctly, do something
    if guessed_letter.get() in secret_word:
        # replace the dashes with the letter
        for i in range(len(secret_word)):
            if list(secret_word)[i] == guessed_letter.get():
                display_word[i] = guessed_letter.get()
        # update your display label with the correct letter
        display.configure(text=display_word)
        # if the user wins what happens???
        # if user guesses word correctly
        if "".join(display_word) == secret_word:
            # update the title label
            title.configure(text="YOU WON")
            # destroy the box where user enters the letter
            letter_entry.destroy()
            # update the play button
            play_button.configure(text="PLAY AGAIN?!")
    else:
        create_hangman_pic(trial)
        trial += 1

        # if the user reaches max number of trials
        if trial == 7:
            messagebox.showwarning("Hangman", "Game Over")
            title.configure(text="YOU LOST!")
            create_hangman_pic(trial=6)
            play_button.configure(text="Play again?!")
            play_button.configure(text="Play again?!", command=root.destroy)
            letter_entry.destroy()
            display.destroy()


# create a button where user can click on and the game will begin
play_button = tk.Button(root,
                        text="LET'S PLAY",
                        command=play_hangman,
                        font="Geneva 20 bold"
                        )
play_button.place(x=150, y=400)

root.mainloop()
