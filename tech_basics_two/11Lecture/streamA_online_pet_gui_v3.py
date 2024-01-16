import tkinter as tk
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


def enter_user_data():
    # create a dictionary with information from the new user page
    user_data = {"name_of_user": name.get(),
                 "username": username.get()
                 }
    user_data = pd.DataFrame([user_data])
    user_data.to_csv("data/user_data.csv", index=False, mode='a', header=False)


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
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage
                         )
    homepage.pack(side=tk.BOTTOM)


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
                               command=lambda:clear_widgets(root)
                               )
    returning_user.pack()

    # if you want to, you can add the create chatbot button here
    #create_chatbot_button(root)

# create the home page
create_homepage()

root.mainloop()