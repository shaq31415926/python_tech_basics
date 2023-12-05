# Reference: https://thecleverprogrammer.com/2020/12/27/music-player-gui-with-python/
# # TODO: Update the title so it shows when user selects

import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame as pg

# create the gui window
root = tk.Tk()

# add title
root.title("Music Gui 🎵")

# configure the size
screen_height = 350
screen_width = 450
root.minsize(width=screen_width, height=screen_height)

# create the directory box
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()  # this gives all the songs in the folder you selected

# creating a list box, that will contain all the songs in the folder I select
play_list = tk.Listbox(root,
                       font="Helvetica 12 bold",
                       bg="yellow",
                       fg="black",
                       selectmode=tk.SINGLE
                       )

# place the song name in the list box
pos = 0
for song in song_list:
    play_list.insert(pos, song)
    pos += 1

# initialise the pygame library
pg.init()


def play_music():
    """This function plays the music when you click on the play button"""

    pg.mixer.music.load(play_list.get(tk.ACTIVE))  # loads the file that you select in your listbox
    #song_label.configure(text=play_list.get(tk.ACTIVE))
    pg.mixer.music.play()


def play_on_selection(event):
    """This function plays the music when you select an item from the list"""
    play_music()
    # will reset the pause button if necessary
    pause_button.configure(text="PAUSE",
                           command=pause_music
                           )


def stop_music():
    """This function stops the music when you click on the stop button"""
    pg.mixer.music.stop()
    # will reset the pause button if necessary
    pause_button.configure(text="PAUSE",
                           command=pause_music
                           )


def pause_music():
    """This function pauses the music when you click on the pause button"""
    pg.mixer.music.pause()
    # this will configure the pause button to become an unpause button
    pause_button.configure(text="UNPAUSE",
                           command=unpause_music
                           )


def unpause_music():
    """This function unpauses the music"""
    pg.mixer.music.unpause()
    # this resets to the pause button
    pause_button.configure(text="PAUSE",
                           command=pause_music
                           )


# creating buttons for my music player gui
# play
play_button = tk.Button(root,
                        text="PLAY",
                        height=3,
                        font="Helvetica 12 bold",
                        bg="blue",  # windows users
                        highlightbackground="blue",  # mac users,
                        highlightthickness="10",
                        fg="black",
                        command=play_music
                        )
# stop
stop_button = tk.Button(root,
                        text="STOP",
                        height=3,
                        font="Helvetica 12 bold",
                        bg="red",  # windows users
                        highlightbackground="red",  # mac users,
                        highlightthickness="10",
                        fg="black",
                        command=stop_music
                        )

# pause
pause_button = tk.Button(root,
                         text="PAUSE",
                         height=3,
                         font="Helvetica 12 bold",
                         bg="purple",  # windows users
                         highlightbackground="purple",  # mac users,
                         highlightthickness="10",
                         fg="black",
                         command=pause_music
                         )

# unpause
unpause_button = tk.Button(root,
                           text="UNPAUSE",
                           height=3,
                           font="Helvetica 12 bold",
                           bg="orange",  # windows users
                           highlightbackground="orange",  # mac users,
                           highlightthickness="10",
                           fg="black",
                           command=unpause_music
                           )

# place the name of the song
#song_name = play_list.get(tk.ACTIVE)
#song_label = tk.Label(root,
#                      font="Hevetica 12 bold",
#                      textvariable=song_name
#                      )
#song_label.pack()

# place the buttons using pack functions
play_button.pack(fill="x")
stop_button.pack(fill="x")
pause_button.pack(fill="x")
play_list.pack(fill="both", expand="True")
# play music on selection
play_list.bind("<<ListboxSelect>>", play_on_selection)

root.mainloop()
