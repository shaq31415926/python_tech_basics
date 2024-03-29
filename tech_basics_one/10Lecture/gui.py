# This code creates a new window with an image
# image, and then create a second window which an image and label

import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Knowledge Check")

# code to configure the size
root.geometry("650x450")


def add_image(root, file_path):
    """This definition will place the image on the gui window.
    You need to specify the variable name that creates your gui window and the image file path"""

    # for some reason this image will not appear without specifying global variables
    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
    img = img.resize((650, 450), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()


# call our add_image function with the root variable image file path
add_image(root, file_path="images/store.jpeg")


# you should see the image appearing in the first screen

def maingame():
    """This definition does the following:
    1. Destroys everything we created in the first window
    2. Adds a new image to the background
    3. Creates a new label
    """

    # destroy all objects we created in first image
    f1.destroy()
    enter_button.destroy()

    # add a new image as the background
    add_image(root, file_path="images/pencils.jpeg")

    # create a label - this will only work after placing the image on the background
    test_label = tk.Label(text=f"Brand One",
                          relief=tk.RAISED,
                          bg='#4834DF',
                          fg='#ffffff',
                          borderwidth=5
                          )
    # if you place a background image, grid does not seem to work to put the labels/buttons
    test_label.place(x=10, y=10)


# add a box on the first gui window, that will clear everything and launch a new page
enter_button = tk.Button(text="Click here to enter store",
                         font='lucida 20 bold',
                         command=maingame,
                         fg="blue")
# play around with the x and y coordinates to place your button
enter_button.place(x=200, y=120)

# check our this script here if you want to add a back button that goes to the first page
# https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_one/10Lecture/gui_v2.py

# code to execute the code
root.mainloop()
