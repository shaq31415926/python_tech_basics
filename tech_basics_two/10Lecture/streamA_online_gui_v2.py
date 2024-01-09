import tkinter as tk
from PIL import Image, ImageTk

# create the GUI
root = tk.Tk()
# update the title of the gui
root.title("Online Pet V2 🐱")

# size the frame
# set the height and width as separate parameters to give you more flexibility
screen_width = 600
screen_height = 400

# option 1: use the minsize function
root.minsize(screen_width, screen_height)  # width, height


# option 2: use the geometry function, and you can also adjust the x and y position
# root.geometry(f'{screen_width}x{screen_height}+550+150')  # width, height, start_x, start_y


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


def clear_widgets():
    """This function will destroy any widgets you created"""
    for i in root.winfo_children():
        i.destroy()


def new_user_page():
    """This function carries out the steps for the new user page"""

    # call the definition that clears all the widgets
    clear_widgets()

    # TODO: add a welcome label

    # TODO: add data entry boxes and labels

    # TODO: create a submit information button

    # add a home page button - this will go back to our home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage
                         )
    homepage.pack(side=tk.BOTTOM)


def create_homepage():
    """This function creates the homepage"""

    # clear widgets in the case widgets have been created
    clear_widgets()

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
    # on activation these buttons should destroy all the widgets
    new_user = tk.Button(root,
                         text="New User",
                         font=("Comic Sans MS", 14, "bold"),
                         command=new_user_page
                         )
    new_user.pack()

    returning_user = tk.Button(root,
                               text="Returning User",
                               font=("Comic Sans MS", 14, "bold"),
                               command=clear_widgets
                               )
    returning_user.pack()


# call my homepage definition to create the home page when launching the gui
create_homepage()

# launch the gui
root.mainloop()
