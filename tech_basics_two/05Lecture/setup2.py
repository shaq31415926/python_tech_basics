import pygame as pg

# initialise the library
pg.init()

# create variables to change colour and size
colour = 192, 192, 192 # this is rgb code - you can adjust this
size = width, height = 500, 400

# create the display
screen = pg.display.set_mode(size)

# you need to execute a while statement to keep the display running
while True:
    for event in pg.event.get():
        # closes the game if the user clicks exit
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # this part will run the steps for the "game"
    screen.fill(colour) # changes the background
    pg.display.update()