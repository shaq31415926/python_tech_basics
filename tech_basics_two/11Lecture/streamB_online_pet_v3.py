import tkinter as tk
from src.streamB_simple_chatbot import create_chatbot_button

# create the gui
root = tk.Tk()
root.title("Online Pet V3")
# size the size
screen_width = 600
screen_height = 400
root.minsize(screen_width, screen_height)

create_chatbot_button(root)

root.mainloop()
