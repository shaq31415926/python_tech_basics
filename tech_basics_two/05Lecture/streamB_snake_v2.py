import pygame as pg
import time
import random

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

game_over = False
# define the variables to format the snake
snake_size = 20
snake_length = 1
snake_coordinates = []

# define the food variables
food_colour = 192, 192, 192
# randomise the x and y coordinates
food_x = round(random.randrange(snake_size+10, disp_width - snake_size)/10) * 10
food_y = round(random.randrange(snake_size+10, disp_height - snake_size)/10) * 10


# create the display screen
screen = pg.display.set_mode(size)
pg.display.set_caption("SNAKE V2")

def display_message(display_text, width, height, screen):
    # select the font
    font = pg.font.SysFont("comicsansms", 60)
    # render the text
    text = font.render(display_text, True, (0, 255, 0), (0, 0, 128))
    # convert into a rectangle object
    textRect = text.get_rect()
    textRect.center = width / 2, height / 2

    # use the blit method to add this surface
    screen.blit(text, textRect)


def display_score(screen, snake_length):
    # select the font
    font = pg.font.SysFont("comicsansms", 24)
    # render the text
    text = font.render(f"The score is {snake_length -1}", True, (255, 255, 102))
    # use the blit method to add this surface
    screen.blit(text, (0, 0))


def play_explosion_music():
    # play some music
    pg.mixer.music.load("music/explosion-6801.mp3")
    pg.mixer.music.play()


def display_snake(snake_coordinates):
    for x in snake_coordinates:
        pg.draw.rect(screen, snake_colour, [x[0], x[1], snake_size, snake_size])


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
        # we will build a game over page next week
        display_message("GAME OVER :(", disp_width, disp_height, screen)
        play_explosion_music()
        pg.display.update()
        time.sleep(3.5)

    screen.fill(background_colour) # changes the background colour
    #pg.draw.rect(screen, food_colour, [food_x, food_y, snake_size-5, snake_size-5])  # code to create food
    apple_image = pg.image.load("images/Apple.png")
    screen.blit(apple_image, (food_x, food_y))

    # store the snake head coordinates
    snake_head = [x1, y1]
    snake_coordinates.append(snake_head)
    display_snake(snake_coordinates)
    #pg.draw.rect(screen, snake_colour, [x1, y1, snake_size, snake_size]) # code to create a rectangle
    if len(snake_coordinates) > snake_length:
        del snake_coordinates[0]

    # if the tail reaches head
    for x in snake_coordinates[:-1]:
        if x == snake_head:
            game_over = True

    display_score(screen, snake_length)

    # what happens when the snake eats the food
    if x1 == food_x and y1 == food_y:
        snake_length += 1
        #print("YUMMY, the snake length is", snake_length)
        # change the position of food
        food_x = round(random.randrange(snake_size + 10, disp_width - snake_size) / 10) * 10
        food_y = round(random.randrange(snake_size + 10, disp_height - snake_size) / 10) * 10
        # play some music
        play_explosion_music()

    pg.display.update()
    clock.tick(30) # adjust the speed, try 30, 60, 120...

# when game_over is True then this will exit the code
pg.quit()
quit()