# Reference:
# https://www.edureka.co/blog/snake-game-with-pygame/

import pygame as pg
import time
import random

# This script contains
# (What we have done so far)
# 1. create the screen
# 2. draw a rectangle - the snake
# 3. move the snake
# 4. creating a game over page when the snake hits the boundary
# 5. adding the food to the game
# 6. displaying the score
# 7. increasing the length
# 8. ending the game when the snake bumps into itself (not tested)
# 9. adding sound effects

# initialise the pygame library
pg.init()

# set some variables
size = disp_width, disp_height = 800, 600
background_colour = 0, 0, 0  # rgb coordinates for black
snake_colour = 255, 0, 0  # rgb coordinates for red
food_colour = 192, 192, 192
# starting position for your snake
x1 = disp_width / 2
y1 = disp_height / 2
# creating variables to move the snake
x1_change = 0
y1_change = 0
# define variables for the snake size
snake_size = 20

# read the apple image
#apple_image = pg.image.load("images/Apple.png")

# add coordinate position for the food - this should be random
food_x = round(random.randrange(30, disp_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(30, disp_height - snake_size) / 10.0) * 10.0
# print(food_x, food_y)

# use the Clock method to control the speed
clock = pg.time.Clock()

# create a game over flag
game_over = False

# create the display screen
screen = pg.display.set_mode(size)
pg.display.set_caption("SNAKE V2")


# create a definition that will give us a game over page when the snake hits the border
def game_over_message(disp_width, disp_height, display_text):
    # create a message that says the user lost
    # set the font - and the size
    font = pg.font.SysFont('arialroundedmtbold.ttf', 60)
    # font = pg.font.Font(None, 32)

    # create a text surface object,on which text is drawn on it.
    text = font.render(display_text, True, (0, 255, 0), (0, 0, 128))
    # the True is for setting smooth edges, the last argument is a background colour

    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object
    textRect.center = (disp_width // 2, disp_height // 2)
    # use the blit method to add the text on the page
    screen.blit(text, textRect)

def play_explosion_music():
    """This function plays explosion music

    This music was downloaded from: https://pixabay.com/sound-effects/search/explosion/"""
    pg.mixer.music.load("music/explosion-6801.mp3")
    pg.mixer.music.play()


# while the game over flag is false, the window stays open
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

    # we want to exit the game if the snake reaches the borders
    if x1 < 0 or y1 < 0 or x1 >= disp_width or y1 >= disp_height:
        game_over = True
        # print a message that tells the user the game is over
        game_over_message(disp_width, disp_height, "GAME OVER")
        # play explosion music
        play_explosion_music()
        # update the display screen with the screen
        pg.display.update()
        # set a timer so the game does not shut down straight away
        time.sleep(5)

    # launch your snake game
    x1 += x1_change  # update the x coordinates
    y1 += y1_change  # update the y coordinates
    screen.fill(background_colour)  # changes the background colour

    # code to create food rectangle
    pg.draw.rect(screen, food_colour, [food_x, food_y, snake_size - 3, snake_size - 3])
    #screen.blit(apple_image, (food_x, food_y))
    pg.draw.rect(screen, snake_colour, [x1, y1, snake_size, snake_size])

    # if the food and snake coordinates match, print something
    if x1 == food_x and y1 == food_y:
        print("yummy")
        play_explosion_music()

    pg.display.flip()
    clock.tick(30)  # adjust the speed, try 30, 60, 120...

# the game is over when the game over flag is set to false
# play some music
pg.quit()
quit()
