import tkinter as tk
from simple_chatbot import create_chatbot_button


# create the gui
root = tk.Tk()
root.title("ChatBot")
# size the size
screen_width = 600
screen_height = 400

# option 1: use the minsize function
root.minsize(screen_width, screen_height)

create_chatbot_button(root)

root.mainloop()