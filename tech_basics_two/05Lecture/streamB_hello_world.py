import pygame as pg

# initialise the library
pg.init()

# create variables to change colour and size
colour = 192, 192, 192 # this is rgb code - you can adjust this
size = width, height = 500, 400

# create the display
screen = pg.display.set_mode(size)

# print the fonts
#print(pg.font.get_fonts())


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


# you need to execute a while statement to keep the display running
while True:
    for event in pg.event.get():
        # closes the game if the user clicks exit
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # this part will run the steps for the "game"
    screen.fill(colour) # changes the background
    # displays a text message of our choice
    display_message("HELLLO WORLD", width, height, screen)

    pg.display.update()
