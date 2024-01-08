import tkinter as tk
from PIL import Image, ImageTk

# create the GUI
root = tk.Tk()
# update the title of the gui
root.title("Online Pet V1 🐱")

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

# add a background to your page - please update the file path depending where your code is located
# if your code is in the lecture folder, then user "images/nameofpicture".
add_image(root, "../images/homepage.jpg", screen_width, screen_height)

# if you have a .png file, you could consider using simplified code from the holiday card gui.

# launch the gui
root.mainloop()