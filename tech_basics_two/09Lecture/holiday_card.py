# Inspiration: https://github.com/Terranova-Python/ChristmasCards/tree/main
import tkinter as tk
import random
import pygame as pg

# Tkinter frames and GUI
root = tk.Tk()
root.title('Holiday Cards')
# you can use the geometry function to also adjust the x and y position
root.geometry('310x400+550+150') # width, height, start_x, start_y

# an easier way to place a background image
# and if you want you can also select a random image
image1 = "images/img1.png"
image2 = "images/img2.png"
image3 = "images/img3.png"
image4 = "images/img4.png"
images = [image1, image2, image3, image4]
# random image
image = random.choice(images)

# this method only accepts GIF, PGM, PPM, and PNG file formats
background_image = tk.PhotoImage(file=image)
background = tk.Label(root, image=background_image)
background.place(x=0, y=0, relwidth=1, relheight=1)  # these attributes ensure it takes up the entire screen

greeting = ["HAPPY HOLIDAYS ☃️", "MERRY XMAS 🎄", "HO! HO! HO! 🎅" ]
# randomise the greetings as well

greeting = random.choice(greeting)
final_label = tk.Label(text=greeting,
                       bg='#ffffff',
                       font=('Calibri', 22, "bold"),
                       fg="black")
final_label.pack(pady=150)

# initialise the pygame library
pg.init()

# add some xmas music
pg.mixer.music.load("music/The Christmas Sleigh Ride.mp3")
pg.mixer.music.play()

root.mainloop()