import pygame as pg
import random
import time

# This script contains
# (What we have done so far)
# 1. create the screen
# 2. draw a rectangle - the snake
# 3. move the snake + ending the game when the snake hits the boundary
# 4. refactoring the code, so we are not using the same code twice
# 5. creating a game over page when the snake hits the boundary
# 6. adding the food to the game
# 7. increasing the length
# 8. displaying the score

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

# snake size
snake_size = 20

# define the food placement
# randomise where we place the food
food_x = round(random.randrange(0, disp_width - snake_size)/10 * 10)
food_y = round(random.randrange(0, disp_height - snake_size)/10 * 10)
food_colour = 192, 192, 192

# add a game over flag
game_over = False

# create the display screen
screen = pg.display.set_mode(size)
pg.display.set_caption("SNAKE V2")

# add some music
#pg.mixer.music.load("music/explosion-6801.mp3")
#pg.mixer.music.play(-1)


def display_text_message(display_text, screen, width, height):
    # set the font
    font = pg.font.SysFont("comicsansms", 72)
    # create a text surface object, on which text is drawn on it. The last argument is the background colour.
    text = font.render(display_text, True, (0, 255, 0), (0, 0, 128))
    # convert into rectangular object
    textRect = text.get_rect()
    # center my text
    textRect.center = (width / 2, height / 2)
    # use the blit method to add the text on the display
    screen.blit(text, textRect)

while game_over is False:
    for event in pg.event.get():
        # closes the game if the user clicks exit
        if event.type == pg.QUIT:
            game_over = True
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

    # launch your snake game
    x1 += x1_change
    y1 += y1_change

    # we want to exit the game if the snake reaches the borders
    if x1 < 0 or y1 < 0 or x1 >= disp_width or y1 >= disp_height:
        game_over = True
        display_text_message("GAME OVER!!!", screen, disp_width, disp_height)
        pg.display.update()
        # add some music
        pg.mixer.music.load("music/explosion-6801.mp3")
        pg.mixer.music.play()

        time.sleep(5)

    screen.fill(background_colour) # changes the background colour
    # create my snake food
    pg.draw.rect(screen, food_colour, [food_x, food_y, snake_size, snake_size])
    pg.draw.rect(screen, snake_colour, [x1, y1, snake_size, snake_size])  # code to create a rectangle

    print(x1, food_x)
    print(y1, food_y)

    # if the snake eats the food, what happens
    if x1 == food_x and y1 == food_y:
        print("yummy")

    pg.display.update()
    clock.tick(15) # adjust the speed, try 30, 60, 120...


pg.quit()
quit()