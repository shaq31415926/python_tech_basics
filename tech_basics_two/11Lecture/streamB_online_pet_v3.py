import tkinter as tk
from src.streamB_simple_chatbot import create_chatbot_button
from src.helpers import clear_widgets, add_image

# create the gui
root = tk.Tk()
root.title("Online Pet V3")
# size the size
screen_width = 600
screen_height = 400
root.minsize(screen_width, screen_height)

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
                         #command=new_user_page
                         )
    new_user.pack()

    returning_user = tk.Button(root,
                               text="Returning User",
                               font=("Comic Sans MS", 14, "bold"),
                               command=lambda:clear_widgets(root)
                               )
    returning_user.pack()

    # chatbot button
    # create_chatbot_button(root)



# call my homepage definition to create the home page when launching the gui
create_homepage()


root.mainloop()
