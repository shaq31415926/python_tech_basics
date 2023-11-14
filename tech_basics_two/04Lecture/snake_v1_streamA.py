import pygame as pg

# initialise pygame
pg.init()

# create some variables
background_colour = 0, 0, 0 # rgb code for black screen
size = dis_width, dis_height = 800, 800
snake_colour = 0, 0, 255 # rgb code for blue
# the starting position for the snake
x1 = dis_width/2
y1 = dis_height/2
# every time the snake moves the x, y coordinates will change
x1_change = 0
y1_change = 0

# create the display screen
# pass in the width and height
screen = pg.display.set_mode(size)
# set a caption
pg.display.set_caption("SNAKE V1")

# control the speed of the snake
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        # add this code to close the window
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pg.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 += x1_change
    y1 += y1_change
    print(x1, y1)

    # FIX: if your snake goes off the screen exit the game
    if x1 < 0 or y1 < 0 or x1 >= dis_width or y1 >= dis_height:
        pg.quit()
        quit()
        # we will pick this up next week

    # running the game
    screen.fill(background_colour)
    # draw your snake
    pg.draw.rect(screen, snake_colour, [x1, y1, 10, 10])

    pg.display.update()
    clock.tick(60)