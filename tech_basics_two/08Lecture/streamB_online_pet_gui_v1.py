import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from datetime import datetime
from tkinter import messagebox

root = tk.Tk()

# update the title
root.title("Online Pet 🐱")

# change the size
screen_width = 600
screen_height = 400
root.minsize(screen_width, screen_height)


def add_image(root, file_path, width, height):
    """This definition will place the image on the gui window.
    You need to specify the variable name that creates your gui window and the image file path"""

    # for some reason this image will not appear without specifying global variables
    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
    img = img.resize((width, height), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()


def enter_user_data():
    # create a timestamp
    current_timestamp = datetime.now()
    # dictionary that stores user data
    user_data = {
        "name": name.get(),
        "user_id": username.get(),
        "created_at": current_timestamp
    }

    # get the list of user ids
    user_ids = list(pd.read_csv("data/users_data.csv").user_id)

    # if the username exists in the csv file, print a warning
    if username.get() in user_ids:
        tk.messagebox.showwarning("WARNING", "This username is taken")
    # otherwise store the users data
    else:
        # converting the dictionary to a data frame
        user_data_df = pd.DataFrame([user_data])
        # write your data frame to a .csv file - since we want to append data we add mode = 'a'
        user_data_df.to_csv("data/users_data.csv", index=False, header=False, mode='a')

        # destroy all widgets that have been created
        for i in root.winfo_children():
            i.destroy()

        # add a thank you
        thankyou_label = tk.Label(root,
                 text=f"Thank you for submitting your data {name.get()}",
                 font=("Comic Sans S", 28, "bold"))
        thankyou_label.pack(side=tk.TOP, anchor=tk.CENTER)

def create_new_user_page():
    global name, username

    # option 1 - DESTROY widgets I created in my home page, dont forget to add these in your global list
    # f1.destroy()
    # welcome_label.destroy()
    # new_user.destroy()
    # returning_user.destroy()

    # option 2 - lists all the widgets that we have created
    for i in root.winfo_children():
        i.destroy()

    # create a home page button
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage)
    homepage.pack(side=tk.BOTTOM)

    # create a welcome label
    new_label = tk.Label(root,
                         text="Welcome New User",
                         font=("Comic Sans MS", 24, "bold"),
                         )
    new_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create some entry boxes to gather information from the user
    name_label = tk.Label(root,
                          text="What is your name?",
                          font=("Comic Sans MS", 20, "bold"),
                          )
    name_label.place(x=50, y=100)

    name = tk.StringVar()
    name_entry = tk.Entry(root,
                          textvar=name,
                          width=10,
                          font=("Comic Sans MS", 20, "bold"),
                          bg="blue",
                          fg="white"
                          )
    name_entry.place(x=260, y=100)

    # create some entry boxes to gather information from the user
    username_label = tk.Label(root,
                              text="Create a user name:",
                              font=("Comic Sans MS", 20, "bold"),
                              )
    username_label.place(x=50, y=150)

    username = tk.StringVar()
    username_entry = tk.Entry(root,
                              textvar=username,
                              font=("Comic Sans MS", 20, "bold"),
                              bg="blue",
                              fg="white"
                              )
    username_entry.place(x=260, y=150)

    # create a button so the user can submit their information
    enter_data = tk.Button(root,
                           text="Create your account",
                           font=("Comic Sans MS", 20, "bold"),
                           highlightbackground="blue",  # mac users,
                           highlightthickness="2",
                           command=enter_user_data)
    enter_data.place(x=200, y=200)


def create_homepage():
    # global welcome_label, new_user, returning_user

    # add code to destroy any widgets that were created for e.g. when you are on the new user page
    for i in root.winfo_children():
        i.destroy()

    # place an image
    add_image(root, "images/homepage.jpg", screen_width, screen_height)

    # place a welcome label
    welcome_label = tk.Label(root,
                             text="WELCOME TO MY ONLINE PET PAGE",
                             font="Arial 20 bold",
                             bg="white",
                             fg="black"
                             )
    welcome_label.place(x=10, y=10)

    # place a new user button
    new_user = tk.Button(root,
                         text="New user",
                         font=("Comic Sans MS", 14, "bold"),
                         command=create_new_user_page
                         )
    new_user.pack()

    # place a returning user button
    returning_user = tk.Button(root,
                               text="Returning user",
                               font=("Comic Sans MS", 14, "bold")
                               )
    returning_user.pack()


# create my home page my calling the create home page definition
create_homepage()

root.mainloop()
