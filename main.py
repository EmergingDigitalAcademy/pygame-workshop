import sys
import pygame

# Initializes the pygame package
pygame.init()

# Define the window size of our application using a tuple

windowSize = (800, 600)

# Define the screen variable and give it the window size defined above

screen = pygame.display.set_mode(windowSize)

# Define the object that controls frame updates

clock = pygame.time.Clock()

# While loop will run the game and determine stop conditions

while True:
    # Define how many frames we want updated per second
    clock.tick(60)

    # Define an event to stop the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

