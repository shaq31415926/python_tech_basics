import tkinter as tk
from tkinter import messagebox
import pandas as pd
from src.helpers import add_image, clear_widgets

# from src.simple_chatbot_v2 import create_chatbot_button

# create the gui
root = tk.Tk()
root.title("Online Pet Gui")
# size the size
screen_width = 600
screen_height = 400

# option 1: use the minsize function
root.minsize(screen_width, screen_height)


# add the add image definition here if needed

# add the clear widgets here if needed

def create_homepage_button():
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage
                         )
    homepage.pack(side=tk.BOTTOM)


def enter_user_data():
    # do a user id check
    # read the username column
    users_ids = list(pd.read_csv("data/user_data.csv").username)

    # checking if usernames exists
    if username.get() in users_ids:
        tk.messagebox.showwarning("WARNING!", "THIS USERNAME ALREADY EXISTS")
    else:
        # create a dictionary with information from the new user page
        user_data = {"name_of_user": name.get(),
                     "username": username.get()
                     }
        # convert the dictionary into a dataframe
        user_data = pd.DataFrame([user_data])
        # write the dataframe to a .csv file
        user_data.to_csv("data/user_data.csv", index=False, mode='a', header=False)

    # clear all the widgets
    clear_widgets(root)

    # thank you label to say information has been submitted
    thankyou_label = tk.Label(root,
                              text="Thanks! Your info has been submitted")
    thankyou_label.place(x=50, y=50)
    # I can add more to this page here...

    # place a homepage button here
    create_homepage_button()


def create_new_userpage():
    """This function carries out the steps for the new user page"""
    global name, username

    # call the definition that clears all the widgets
    clear_widgets(root)

    # create a welcome label
    new_label = tk.Label(root,
                         text="WELCOME NEW USER!!",
                         font=("Comic Sans MS", 28, "bold"))
    new_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # Create labels and entry boxes to get user information
    # ask for the name of the user
    name_label = tk.Label(root,
                          text="What is your name?!",
                          fg="white"
                          )
    name_label.place(x=50, y=100)

    # entry box
    name = tk.StringVar()
    name_box = tk.Entry(root,
                        textvar=name,
                        fg="white",
                        bg="blue"
                        )
    name_box.place(x=200, y=100)

    # ask for a user name
    username_label = tk.Label(root,
                              text="Create a user name",
                              fg="white"
                              )
    username_label.place(x=50, y=150)

    # entry box
    username = tk.StringVar()
    username_box = tk.Entry(root,
                            textvar=username,
                            fg="white",
                            bg="blue"
                            )
    username_box.place(x=200, y=150)

    # TODO: create a submit information button
    # create a button to store all the information
    enter_data = tk.Button(root,
                           text="SUBMIT INFO",
                           command=enter_user_data
                           )
    enter_data.place(x=250, y=200)

    # add a home page button - this will go back to our home page
    create_homepage_button()


def check_user():
    # read all the usernames
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    # check if username exists - then go onto next page
    if user_id.get() in user_ids:
        clear_widgets(root)
        create_homepage_button()
        # ADD MORE CODE
   # otherwise give a warning
    else:
        tk.messagebox.showwarning("WARNING", "User does not exist")


def create_returning_userpage():
    global user_id

    # clear widgets
    clear_widgets(root)

    # entry box to ask for the username
    # ask for a user name
    userid_label = tk.Label(root,
                              text="Enter your user name",
                              fg="white"
                              )
    userid_label.place(x=50, y=150)

    # entry box
    user_id = tk.StringVar()
    userid_box = tk.Entry(root,
                            textvar=user_id,
                            fg="white",
                            bg="blue"
                            )
    userid_box.place(x=200, y=150)

    # add a button to login
    login_button = tk.Button(root,
              text="login",
              command=check_user
              )
    login_button.place(x=250, y=200)

    # place a homepage button
    create_homepage_button()


def create_homepage():
    """This function creates the homepage"""

    # clear widgets in the case widgets have been created
    clear_widgets(root)

    # create the home page background
    add_image(root, "images/homepage.jpg", screen_width, screen_height)

    # add a welcome label
    welcome_label = tk.Label(root,
                             text="WELCOME TO MY ONLINE PET PAGE",
                             font="Arial 20 bold",
                             fg="black",
                             bg="white"
                             )
    welcome_label.place(x=10, y=10)

    # add two buttons new and returning user
    # on activation these buttons should destroy all the widgets and carry out the steps for the page
    new_user = tk.Button(root,
                         text="New User",
                         font=("Comic Sans MS", 14, "bold"),
                         command=create_new_userpage
                         )
    new_user.pack()

    returning_user = tk.Button(root,
                               text="Returning User",
                               font=("Comic Sans MS", 14, "bold"),
                               command=create_returning_userpage
                               )
    returning_user.pack()

    # if you want to, you can add the create chatbot button here
    # create_chatbot_button(root)


# create the home page
create_homepage()

root.mainloop()
