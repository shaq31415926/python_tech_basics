import tkinter as tk
from PIL import Image, ImageTk

# creating our graphical user interface
root = tk.Tk()

# give your gui a title
root.title("Rock Paper Scissors Game!!!")

# change the size of the gui
root.geometry("650x450")

# change the colour of the gui
# root.configure(background='pink')

f1 = tk.Frame(root)
# read the image
img = Image.open("images/rps.jpeg")
# resize the image
img = img.resize((650, 450), Image.LANCZOS)
# add the image to your gui
pic = ImageTk.PhotoImage(img)
Lab = tk.Label(f1, image=pic)
Lab.pack()
f1.pack()


root.mainloop()