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
    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image
    img = img.resize((650, 450), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()


add_image(root, file_path="images/store.jpeg")

def maingame():
    f1.destroy()
    enter_button.destroy()

    # add_image(root, file_path="images/pencils.jpeg")

    # create a label
    test_label = tk.Label(text=f"Brand One",
                          relief=tk.RAISED,
                          bg='#4834DF',
                          fg='#ffffff',
                          borderwidth=5
                          )
    test_label.place(x=10, y=10)


# add a box, that will clear everything and launch a new gui window
enter_button = tk.Button(text="Click here to enter store",
                         font='lucida 20 bold',
                         command=maingame,
                         fg="blue")
enter_button.place(x=200, y=120)

# code to execute the code
root.mainloop()
