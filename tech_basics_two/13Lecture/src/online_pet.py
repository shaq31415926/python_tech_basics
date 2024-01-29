import tkinter as tk

# This code was inspired by: https://thecleverprogrammer.com/2021/01/24/screen-pet-with-python/#google_vignette

def online_pet(root):
    c = tk.Canvas(root, width=400, height=400)
    c.configure(bg='dark blue', highlightthickness=0)
    c.body_color = 'SkyBlue1'

    c.pack()