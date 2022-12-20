import sys

import pygame

# Initializes the pygame package
pygame.init()

# Define the window size of our application using a tuple
windowSize = (800, 600)

# Define the screen variable and give it the window size defined above
screen = pygame.display.set_mode(windowSize)

# Initializes the EDA logo to load in the game
edaLogoLarge = pygame.image.load("static/eda-icon.png")

# New width and height will be (50, 30).
edaLogo = pygame.transform.scale(edaLogoLarge, (100, 70))

# Get the size of the logo item
edaLogoSize = edaLogo.get_size()

# Define starting coordinates and starting movement directions for the logo item
# Positive movement directions will mean the logo will move right or down on the
# Screen, negative will make the logo move left or up
x, y = 0, 0

# Define the object that controls frame updates
clock = pygame.time.Clock()

# While loop will run the game and determine stop conditions
while True:
    # Define how many frames we want updated per second
    clock.tick(60)

    # Define a background color for our screen
    screen.fill((38, 39, 95))

    # Get Mouse position to control the logo with the mouse
    mousePosition = pygame.mouse.get_pos()

    # Set x and y coordinates to the mouse position
    x, y = (mousePosition[0] - edaLogoSize[0] / 2), (mousePosition[1] -
                                                     edaLogoSize[1] / 2)

    # Paste the logo item onto the screen along with the starting coordinates
    screen.blit(edaLogo, (x, y))

    # Update the display every tick
    pygame.display.update()

    # Define an event to stop the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
