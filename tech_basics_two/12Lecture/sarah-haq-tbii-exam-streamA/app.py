import tkinter as tk
from src.helpers import set_background, clear_widgets

# create the gui frame
root = tk.Tk()
root.title("Sample GUI")
# size the size of the frame
screen_width = 1000
screen_height = 600

# option 1: use minsize
root.minsize(screen_width, screen_height)

# option 2: use geometry, if you want to position where the gui frame launches
#root.geometry(f'{screen_width}x{screen_height}+550+150')  # width, height, start_x, start_y


def create_new_page(root):
    """This function creates a new page that will clear all the widgets
    that were previously generated, changes the background colour and places a button that will go back"""

    # clears the widgets - the image and the button
    clear_widgets(root)

    # change the background colour of the frame
    root.configure(background="pink")

    # place a button that will go back
    back_button = tk.Button(root,
                            text="GO BACK",
                            font=("Comic Sans MS", 14, "bold"),
                            command=lambda: create_homepage(root, image_file_path="image/homepage.jpeg")
                            )

    back_button.place(relx=0.5,
                      rely=0.925)

    # We covered this in TBI - a button that closes the game
    exit_button = tk.Button(text="X",
                            font=("Comic Sans MS", 14, "bold"),
                            command=root.destroy
                            )
    exit_button.pack(side="bottom", anchor='e')
    exit_button.place(relx=0.6,
                      rely=0.925)


def create_homepage(root, image_file_path):
    """This definition creates the homepage.
    It places a background image and places a button at the bottom"""

    # place a background image on the home page using the set background definition
    set_background(root, image_file_path)

    # place a button that will go a new page
    newpage_button = tk.Button(root,
                               text="CLICK HERE TO GO TO THE NEXT PAGE",
                               font=("Comic Sans MS", 14, "bold"),
                               command=lambda: create_new_page(root)
                               )
    newpage_button.pack(side="bottom")


# calling the function that creates the homepage
image_file_path = "image/homepage.jpeg"
create_homepage(root, image_file_path)

# this code is necessary to launch and run the gui
root.mainloop()