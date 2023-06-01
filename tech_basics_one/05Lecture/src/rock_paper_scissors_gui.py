# import the libraries that we will be working with
import tkinter as tk
from PIL import Image, ImageTk

# create the graphical user interfacce
root = tk.Tk()

# give your gui a title
root.title('Rock Paper Scissor')

# set the configuration of GUI window
root.geometry("650x450")

# Create the frame for the first windows of the game
f1 = tk.Frame(root)
# read the image you want to use for the first fra,e
img = Image.open('images/rps.jpeg')
# resize the image
img = img.resize((650, 450), Image.LANCZOS)
# add this code to view the image as the frame
pic = ImageTk.PhotoImage(img)
Lab = tk.Label(f1, image=pic)
Lab.pack()
f1.pack()

# add buttons to your first frame so the user can add their name
# Create some widgets and place them above the image

# print a message asking the user for their name
name = tk.Label(root, text='Please Enter Your Name :', font='arial 15 bold')
# where would you like to place this button
name.place(x=230, y=20)
# This variable will store the name of user
nameinp = tk.StringVar()

root.mainloop()
