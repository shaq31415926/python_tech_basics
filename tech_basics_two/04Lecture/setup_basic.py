import pygame as pg

# initialise the library
pg.init()

# create variables to change colour and size
colour = 192, 192, 192
size = width, height = 500, 400

# create the display
screen = pg.display.set_mode(size)
# update the caption
pg.display.set_caption("SETTING UP")


# optional - creating a surface
surface1 = pg.Surface((100, 50))
surface1.fill((255, 0, 0))

while True:
    for event in pg.event.get():
        # closes the game if the user clicks exit
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # this part will run the "game"
    screen.fill(colour) # changes the background
    screen.blit(surface1, (20, 20)) # optional, this places the surface
    pg.display.update()