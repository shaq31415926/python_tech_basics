import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
from tkinter import messagebox

# create the gui window
root = tk.Tk()

# update the title of the gui
root.title("Online Pet V1 🐱")

# configure the size
screen_width = 600
screen_height = 400
root.minsize(screen_width, screen_height)


# page 1
# add a background image
# add two buttons - new and returning user
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

    current_timestamp = datetime.now()

    # create a dictionary that stores the information the user enters and a timestamp field
    user_data = {
        "name_of_user": name.get(),
        "user_id": username.get(),
        "created_at": current_timestamp
    }

    # read the list of existing user ids
    user_ids = list(pd.read_csv("data/users_data.csv").user_id)

    # if the username exists then print a warning box
    if username.get() in user_ids:
        tk.messagebox.showwarning("WARNING!", "This username already exists")
    # otherwise write the data to the .csv file and do more
    else:
        # convert the dictionary into a data frame
        user_data_df = pd.DataFrame([user_data])
        # write to a csv file - to add future iterations of data we set mode to append and header to be false
        user_data_df.to_csv("data/users_data.csv", index=False, mode='a', header=False)

        # clear all the widgets that were created
        # option 2
        for i in root.winfo_children():
            i.destroy()

        # add a thank you label
        thankyou_label = tk.Label(root,
                                  text=f"Thank you {name.get()}",
                                  font=("Comic Sans MS", 28, "bold"))
        thankyou_label.pack(side=tk.TOP, anchor=tk.CENTER)


def create_new_user_page():
    global homepage, name_label, username_label, username_box, name_box, new_label, username, name

    # destroy everything we created in our homepage
    # specify the widgets
    #f1.destroy()
    #welcome_label.destroy()
    #new_user.destroy()
    #returning_user.destroy()
    # use this loop to destroy everything that was created
    for i in root.winfo_children():
        i.destroy()

    # create a button for the users to go back to the home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage
                         )
    homepage.pack(side=tk.BOTTOM)

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


def create_homepage():
    """This creates the home page with a background image and a welcome label, new and returning user button"""
    global welcome_label, new_user, returning_user

    # handy bit of code to clear all widgets created on previous screens
    for i in root.winfo_children():
        i.destroy()

    # steps to create my home page
    # add a background to your first page
    add_image(root, "images/homepage.jpg", screen_width, screen_height)

    # create a label
    welcome_label = tk.Label(root,
                             text="WELCOME TO MY ONLINE PETS PAGE",
                             font="Arial 20 bold",
                             fg="black",
                             bg="white")
    welcome_label.place(x=10, y=10)

    # create a new user button
    new_user = tk.Button(root,
                         text="New User",
                         font=("Comic Sans MS", 14, "bold"),
                         command=create_new_user_page
                         )
    # create a returning user button
    returning_user = tk.Button(root,
                               text="Returning User",
                               font=("Comic Sans MS", 14, "bold"))

    new_user.pack()
    returning_user.pack()


# create the home page
create_homepage()

# launch the gui window
root.mainloop()
