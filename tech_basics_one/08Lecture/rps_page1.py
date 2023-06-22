import tkinter as tk
from PIL import Image, ImageTk

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Rock Paper Scissors")

# code to configure the size
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

# print a message asking the user for their name
name = tk.Label(root, text='Please Enter Your Name :', font='arial 15 bold')
# where would you like to place this button
name.place(x=230, y=20)

# create an entry box to store the users name
nameinp = tk.StringVar() # This variable will store the name of user
inpname = tk.Entry(root, textvar=nameinp, font='arial 15 bold')
inpname.place(x=230, y=60)


# code to execute the code
root.mainloop()


