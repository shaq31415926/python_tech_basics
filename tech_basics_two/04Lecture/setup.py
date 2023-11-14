import pygame as pg

# initialise our pygame library
pg.init()

# creating the screen of a specific width and height
screen = pg.display.set_mode((400, 500))
# set a caption
pg.display.set_caption("SETTING UP")
# create a colour variable
colour = 255, 0, 0 # rgb coordinates of your choice

surface1 = pg.Surface((100, 50))
surface2 = pg.Surface((50, 50))
surface3 = pg.Surface((50, 100))

surface1.fill((192, 192, 192))
surface2.fill((0, 255, 0))
surface3.fill((0, 0, 255))


while True:
    for event in pg.event.get():
        # close the game if someone clicks on the exit button
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # running our game
    # to change the colour of the background, pass in rgb coordinates of your choice
    screen.fill(colour)
    # add our surface to the display
    screen.blit(surface1, (20, 20))
    screen.blit(surface2, (100, 100))
    screen.blit(surface3, (200, 80))

    # to launch the display screen
    pg.display.update()