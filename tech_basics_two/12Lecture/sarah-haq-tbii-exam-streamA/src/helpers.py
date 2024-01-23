from PIL import Image,ImageTk
import tkinter as tk


def set_background(root, image_file_path):
    """This function was inspired by Robin Paul and sets the background image

    You need to specify the variable that creates the gui frame and the file path of the image
    """

    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)


def clear_widgets(root):
    """This function will destroy any widgets you created

    You need to specify the variable that creates the gui frame
    """
    for i in root.winfo_children():
        i.destroy()


