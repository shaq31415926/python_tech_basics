import pygame as pg

# initialise the library
pg.init()

# create some variables with colour and sizes
size = width, height = 300, 200
colour = 0, 0, 0
speed = [5, 5]

# creating the display screen
screen = pg.display.set_mode(size)
# set the caption
pg.display.set_caption("MY FIRST GAME")

# place the image on our display
ball = pg.image.load("images/intro_ball.gif")
# convert this image into a rectangular object
ballrect = ball.get_rect()

# load some music
pg.mixer.music.load("music/test.mp3")
pg.mixer.music.play(-1)

while True:
    for event in pg.event.get():
        # close the game if someone clicks on the exit button
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # move my ballrect
    ballrect = ballrect.move(speed)

    # if else statement to reverse the speed coordinates when it reaches the boundaries
    # we will break this out in the snake game, reference for the code:
    # Reference: https://www.pygame.org/docs/tut/PygameIntro.html
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # code to run my game
    screen.fill(colour)  # changes the background colour
    screen.blit(ball, ballrect)  # place the image on the display
    pg.display.update()
