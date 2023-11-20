import pygame as pg

# initialise the pygame library
pg.init()

# set some variables
size = disp_width, disp_height = 800, 600
background_colour = 0, 0, 0 # rgb coordinates for black
snake_colour = 255, 0, 0 # rgb coordinates for red
# starting position for your snake
x1 = disp_width/2
y1 = disp_height/2
# creating variables to move the snake
x1_change = 0
y1_change = 0
# use the Clock method to control the speed
clock = pg.time.Clock()


# create the display screen
screen = pg.display.set_mode(size)
pg.display.set_caption("SNAKE V1")

while True:
    for event in pg.event.get():
        # closes the game if the user clicks exit
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

    # FIX: we want to exit the game if the snake reaches the borders
    if x1 < 0 or y1 < 0 or x1 >= disp_width or y1 >= disp_height:
        pg.quit()
        quit()
        # we will build a game over page next week

    # launch your snake game
    x1 += x1_change
    y1 += y1_change
    screen.fill(background_colour) # changes the background colour
    pg.draw.rect(screen, snake_colour, [x1, y1, 10, 10]) # code to create a rectangle
    pg.display.update()
    clock.tick(30) # adjust the speed, try 30, 60, 120...