import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame as pg

# TODO: Update the title so it shows when user selects

# create my gui window
root = tk.Tk()

# create a title
root.title("Music Gui 🎵")

# configure the size
screen_height = 350
screen_width = 450
root.minsize(width=screen_width, height=screen_height)

# ask the user to select the folder that contains music
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()  # lists the songs in the directory the music selects

# create a list box
play_list = tk.Listbox(root,
                       font="Helvetica 14 bold",
                       bg="yellow",
                       fg="black",
                       selectmode=tk.SINGLE
                       )
# this adding the songs to the list box
pos = 0
for song in song_list:
    play_list.insert(pos, song)
    pos += 1

# initialise the pygame library
pg.init()


def play_music():
    """This plays the music when you click on the play button"""

    pg.mixer.music.load(play_list.get(tk.ACTIVE))
    pg.mixer.music.play()
    # set the song name at the top
    song_name.set(play_list.get(tk.ACTIVE))
    # reset the pause button if needed
    pause_button.configure(text="PAUSE",
                           command=pause_music
                           )


def play_on_selection(event):
    """This plays this music when you select from the listbox"""

    play_music()


def stop_music():
    """This stops the music when you click on the stop button"""

    pg.mixer.music.stop()
    # reset the pause button if needed
    pause_button.configure(text="PAUSE",
                           command=pause_music
                           )


def pause_music():
    """This pauses the music when you click on the pause button and then updates to unpause"""
    pg.mixer.music.pause()
    pause_button.configure(text="UNPAUSE",
                           command=unpause_music
                           )


def unpause_music():
    """This unpauses the music after the user selects pause"""

    pg.mixer.music.unpause()
    pause_button.configure(text="PAUSE",
                           command=pause_music
                           )


# creating the button for our gui
# play button
play_button = tk.Button(root,
                        text="PLAY",
                        height=3,
                        font="Helvetica 14 bold",
                        fg="black",
                        # bg="blue", # windows user,
                        highlightbackground="blue",  # mac users can adjust the border thickness
                        highlightthickness=10,
                        command=play_music
                        )

# stop button
stop_button = tk.Button(root,
                        text="STOP",
                        height=3,
                        font="Helvetica 14 bold",
                        fg="black",
                        # bg="blue", # windows user,
                        highlightbackground="red",  # mac users can adjust the border thickness
                        highlightthickness=10,
                        command=stop_music
                        )

# pause button
pause_button = tk.Button(root,
                         text="PAUSE",
                         height=3,
                         font="Helvetica 14 bold",
                         fg="black",
                         # bg="blue", # windows user,
                         highlightbackground="purple",  # mac users can adjust the border thickness
                         highlightthickness=10,
                         command=pause_music
                         )

# place the name of the song
# this does not work well when you select the song from selection
song_name = tk.StringVar()
song_title = tk.Label(root,
                      font="Helvetica 12 bold",
                      textvariable=song_name)
song_title.pack()


# place the buttons using pack function
play_button.pack(fill="x")
stop_button.pack(fill="x")
pause_button.pack(fill="x")
play_list.pack(fill="both", expand=True)
# play music on selection
play_list.bind("<<ListboxSelect>>", play_on_selection)


# launch my gui
root.mainloop()
