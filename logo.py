# ICS3U
# Assignment 2: Logo
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine and import math for an arc
import math
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
RED = (200, 16, 46)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 47, 108)
GREEN = (96, 128, 56)
# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(GREEN)

    # Queue different shapes and lines to be drawn
    pygame.draw.ellipse(screen, BLUE, [50, 50, 300, 300], 0)
    pygame.draw.ellipse(screen, WHITE, [90, 90, 225, 225], 0)
    pygame.draw.ellipse(screen, RED, (102, 102, 200, 200),0)
    pygame.draw.ellipse(screen, WHITE, (140, 140, 125, 125),0)
    pygame.draw.polygon(screen, WHITE, [[200, 200], [275, 125],[275, 275]], 0)
    pygame.draw.rect(screen, WHITE, [275, 135, 18, 135])
    pygame.draw.rect(screen, WHITE, [275, 160, 30, 85])
    font = pygame.font.Font(None, 110)
    text = font.render("UBS", -200, RED)
    screen.blit(text, (150, 175))
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
