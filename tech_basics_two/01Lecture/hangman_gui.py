# code reference:
# https://github.com/codebiet/Hangman/blob/main/hangman.py
# https://github.com/MartinGurasvili/Python-Tkinter-Hangman/blob/main/hangman.py

import tkinter as tk
from PIL import Image, ImageTk
from string import ascii_uppercase
import random

# code to create the gui window
root = tk.Tk()
# code to create a title
root.title("Hangman")
# code to change the size
root.minsize(width=450, height=450)
root.configure(background="black")

# add a label that says guess the letter
title = tk.Label(root,
                 text='Guess The Letter',
                 fg="red",
                 font="Geneva 30 bold")
# place the label
title.place(x=100, y=0)
# title.pack()

# add a label that will add the dashes
# you will also need the code that creates the random word
# definition that generates random word
def get_random_word(word_list):
    random_word = random.choice(word_list)

    return random_word

word_list = ["cat", "dog", "sweet"]
secret_word = get_random_word(word_list)

# create a variable that prints dashes instead of secret word
display_secret_word =  list("_"*len(secret_word))
display_secret_word = " ".join(display_secret_word)

display = tk.Label(root, text=display_secret_word, fg="white",font="Geneva 40",bg="#282828")
display.place(x=140, y=50)

# add a button so the user can enter a letter
guessed_letter = tk.StringVar()
letter_box = tk.Entry(root,
                  textvariable=guessed_letter,
                  fg="white",
                  font="Geneva 25 bold",
                  bg="#282828")
letter_box.place(x=50, y=350)

# problem: we can not cap how many letters a user insert, so an alternative would be to create buttons with letters the player can select
# to be completed - as need to place
#n=0
#for c in ascii_uppercase:
 #   letter_button = tk.Button(root,
  #            text=c,
              # command=lambda c=c: guess(c),
   #           font=('Arial 18'),
    #          width=4)
    #letter_button.grid(row=100+n//9,column=n%9)
    #n+=1

# create a canvas
canvas= tk.Canvas(root, width= 250, height= 200, bg='white')
canvas.place(x=110, y=140)

# on this canvas place an intro image
img = ImageTk.PhotoImage(file="images/intro.png")
canvas.create_image(130, 110, image=img)


def play_hangman():
    print("the letter guessed is", guessed_letter.get())

    # we will pick this up next week


# create a button that will enter the hangman game
# create a box that when you click on will enter the second page
play_button = tk.Button(
              text="LET'S PLAY",
              command=play_hangman,
              font="Geneva 20 bold",
)
play_button.place(x=150, y=400)



root.mainloop()