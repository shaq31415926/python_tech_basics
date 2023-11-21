import pygame as pg

# initialise the library
pg.init()

# create variables to change colour and size
colour = 192, 192, 192  # this is rgb code - you can adjust this
size = width, height = 500, 400

# create the display
screen = pg.display.set_mode(size)
# create a caption
pg.display.set_caption("HELLO WORLD")


# check the fonts available
# print(pg.font.get_fonts())

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


# you need to execute a while statement to keep the display running
while True:
    for event in pg.event.get():
        # closes the game if the user clicks exit
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # this part will run the steps for the "game"
    screen.fill(colour)  # changes the background

    display_text_message("Hello, World!!", screen, width, height)

    pg.display.update()
