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


# code to execute the code
root.mainloop()


