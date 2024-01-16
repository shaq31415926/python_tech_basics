import tkinter as tk
from tkinter import messagebox
import pandas as pd
from src.streamB_simple_chatbot import create_chatbot_button
from src.helpers import clear_widgets, add_image

# create the gui
root = tk.Tk()
root.title("Online Pet V3")
# size the size
screen_width = 600
screen_height = 400
root.minsize(screen_width, screen_height)

# create a homepage button definition
def create_homepage_button():
   homepage = tk.Button(root,
                        text="🏠",
                        command=create_homepage
                        )
   homepage.pack(side=tk.BOTTOM)


def user_check():
    # check if user exists
    user_ids = list(pd.read_csv("data/users_data.csv").user_id)
    # if user exists - go to next page
    if user_id.get() in user_ids:
        clear_widgets(root)
    # otherwise give error
    else:
        tk.messagebox.showwarning("Warning!!", "Please register as a new user")



def create_return_userpage():
    global user_id
    # clear the widgets
    clear_widgets(root)

    # ask for some user data
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

    # create a login button
    login_button = tk.Button(root,
              text="Login",
              command=user_check
              )
    login_button.place(x=200, y=190)

    # place the homepage button
    create_homepage_button()



def enter_user_data():
    # add validation
    # read the .csv file to identify all the user ids that have been created
    # NOTE: If this errors, you may need to create a .csv file in a data folder with the headers name_of_user,user_id
    user_ids = list(pd.read_csv("data/users_data.csv").user_id)

    if username.get() in user_ids:
        tk.messagebox.showwarning("WARNING", "THIS USERNAME ALREADY EXISTS!!!")
    else:
        # capture the data from the entry boxes as a dictionary
        user_data = {"name_of_user": name.get(),
                     "user_id": username.get()
                     }
        # convert to a data frame
        user_data = pd.DataFrame([user_data])
        # write as a .csv file in the data folder
        user_data.to_csv("data/users_data.csv", index=False, mode='a', header=False)

        # steps to create your next page, which you can wrap into a definition and then call the definitions...
        # clear the widgets
        clear_widgets(root)

        # place a label
        thankyou_label = tk.Label(root,
                                  text="Thank you for submitting for your info")
        thankyou_label.place(x=50, y=50)

        # add the homepage button
        create_homepage_button()


# create your new user page definition
def create_new_userpage():
    global username, name

    # clear widgets
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

    # create a button to store all the information
    enter_data = tk.Button(root,
                           text="SUBMIT INFO",
                           command=enter_user_data
                           )
    enter_data.place(x=250, y=200)

    # add a homepage button
    create_homepage_button()


# CREATE A DEFINITION THAT WILL CREATE YOUR HOMPAGE
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
                               command=create_return_userpage
                               )
    returning_user.pack()

    # chatbot button
    # create_chatbot_button(root)



# call my homepage definition to create the home page when launching the gui
create_homepage()


root.mainloop()
