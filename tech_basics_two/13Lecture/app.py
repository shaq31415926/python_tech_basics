import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
from src.helpers import set_background, clear_widgets
from src.online_pet import online_pet

# create the gui frame
root = tk.Tk()
root.title("Online Pet MVP")
# size the size of the frame - you only need to do this once, unless you are playing around with resizing images
screen_width = 500
screen_height = 400
# option 1: use minsize to adjust the screen
root.minsize(screen_width, screen_height)
# option 2: use geometry, if you want to position where the gui frame launches
# root.geometry(f'{screen_width}x{screen_height}+550+150')  # width, height, start_x, start_y


def new_page_setup(root):
    """This function will do the following every time you create a new page:

    1. Clear all the widgets that have been created
    2. Place a button that will go back to the homepage every time you click on it
    """

    # this clear all the widgets that have been created
    clear_widgets(root)

    # add a home page button - this will go back to our home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=lambda: create_homepage(root)
                         )
    homepage.pack(side=tk.BOTTOM)


def create_online_pet_page(root):
    new_page_setup(root)
    online_pet(root)

    # this will place an exit button
    exit_button = tk.Button(text="X",
                            font=("Comic Sans MS", 14, "bold"),
                            command=root.destroy
                            )
    exit_button.pack(side="bottom", anchor='e')
    exit_button.place(relx=0.9,
                      rely=0.925)


def check_user(root):
    """This will check if the user exists before moving on to the online pet page"""

    # before moving onto the next page, I am checking if the user exists
    # this is overkill for your MVPs but I just wanted to show how you can read user_data and

    # read all the usernames in the username from the .csv file
    user_ids = list(pd.read_csv("user_data/users_data.csv").user_id)

    # check if username exists - then go onto next page
    if username.get() in user_ids:
        create_online_pet_page(root)
    # otherwise give a warning
    else:
        tk.messagebox.showwarning("WARNING", "User does not exist")


def create_returning_user_page(root):
    global username
    # if you are creating a widget or a variable and you need to use this in another function or part of the code create a global variable

    new_page_setup(root)

    # entry box to ask for the username
    # ask for a user name
    userid_label = tk.Label(root,
                            text="Enter your user name",
                            fg="white"
                            )
    userid_label.place(x=50, y=150)

    # entry box
    username = tk.StringVar()
    username_box = tk.Entry(root,
                          textvar=username,
                          fg="white",
                          bg="blue"
                          )
    username_box.place(x=200, y=150)

    # add a button to login
    login_button = tk.Button(root,
                             text="Login",
                             command=lambda:check_user(root)
                             )
    login_button.place(x=225, y=200)


def enter_user_data():
    """This function will capture and store all the data from the new user"""

    # this will keep track of when the user registered
    current_timestamp = datetime.now()

    # create a dictionary that stores the information the user enters and a timestamp field
    user_data = {
        "name_of_user": name.get(),
        "user_id": username.get(),
        "created_at": current_timestamp
    }

    # read the list of existing user ids
    user_ids = list(pd.read_csv("user_data/users_data.csv").user_id)

    # this is overkill for your MVPs but additional validation to make sure the user does not enter nothing
    if len(username.get()) == 0 and len(name.get()) == 0:
        messagebox.showerror('Error', 'Please enter a name and username!')
    elif len(name.get()) == 0:
        messagebox.showerror('Error', 'Please enter your name!')
    elif len(username.get()) == 0:
        messagebox.showerror('Error', 'Please enter a user name!')
    else:
        # if the username exists then print a warning box
        if username.get() in user_ids:
            tk.messagebox.showwarning("WARNING!", "This username already exists")
        # otherwise write the user_data to the .csv file and then move onto the next page
        else:
            # convert the dictionary into a user_data frame
            user_data_df = pd.DataFrame([user_data])
            # write to a csv file - to add future iterations of user_data we set mode to append and header to be false
            user_data_df.to_csv("user_data/users_data.csv", index=False, mode='a', header=False)
            # clear the widgets and place the homepage button
            new_page_setup(root)
            # add a thank you label
            thankyou_label = tk.Label(root,
                                      text=f"Thank you {name.get().capitalize()}",
                                      font=("Comic Sans MS", 28, "bold"))
            thankyou_label.pack(side=tk.TOP, anchor=tk.CENTER)

            # place a button to go to the online pet page
            visit_pet_button = tk.Button(root,
                                         text="Click here to visit your pet 🐈",
                                         font=('Comic Sans MS', 18, 'bold'),
                                         command=lambda:create_online_pet_page(root))
            visit_pet_button.pack()


def create_new_user_page(root):
    global username, name # we globalise these variables as we want to store them in a .csv file

    new_page_setup(root)

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

    # create a button to store all the information
    enter_data = tk.Button(root,
                           text="SUBMIT INFO",
                           command=enter_user_data
                           )
    enter_data.place(x=200, y=200)


def create_homepage(root):
    """This definition creates the homepage.

    It places a background image, a label and places some buttons at the bottom
    """

    # If you are placing a homepage button that will go back to the homepage then you will need to clear the widgets
    # otherwise this code is not required
    clear_widgets(root)

    # place a background image on the home page using the set background definition
    # I am hard coding the values were as these are specific to the home page and will not be used anywhere else
    set_background(root, "image/homepage.jpeg", background_colour="white")

    # add a welcome label
    welcome_label = tk.Label(root,
                             text="WELCOME TO MY ONLINE PET PAGE",
                             font="Arial 20 bold",
                             fg="black",
                             bg="white"
                             )
    welcome_label.place(relx=0.12)

    # place a button that will go a new user page
    new_user = tk.Button(root,
                         text="NEW USER",
                         font=("Comic Sans MS", 14, "bold"),
                         command=lambda: create_new_user_page(root)
                         )
    new_user.place(relx=0.2, rely=0.92)

    # place a button that will go a new user page
    returning_user = tk.Button(root,
                               text="RETURNING USER",
                               font=("Comic Sans MS", 14, "bold"),
                               command=lambda: create_returning_user_page(root)
                               )
    returning_user.place(relx=0.45, rely=0.92)


# calling the function that creates the homepage
create_homepage(root)

# this code is necessary to launch and run the gui
root.mainloop()
