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
edaLogo = pygame.transform.scale(edaLogoLarge, (150, 105))

# Define starting coordinates and starting movement directions for the logo item
# Positive movement directions will mean the logo will move right or down on the
# Screen, negative will make the logo move left or up
x, y = 0, 0
directionX, directionY = 1, 1

# Define the object that controls frame updates
clock = pygame.time.Clock()

# While loop will run the game and determine stop conditions
while True:
    # Define how many frames we want updated per second
    clock.tick(60)

    # Define a background color for our screen
    screen.fill((38, 39, 95))

    # Increment the x coordinate by 5 every frame update
    x += 5

    # Paste the logo item onto the screen along with the starting coordinates
    screen.blit(edaLogo, (x, y))

    # Update the display every tick
    pygame.display.update()

    # Define an event to stop the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
