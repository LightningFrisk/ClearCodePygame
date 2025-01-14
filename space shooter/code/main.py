# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init() #initializes pygame, needed for things to run properly
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption("Space Shooter by Tripothy")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #defines window w/ size and such
clock = pygame.time.Clock() #clock
running = True #bool that makes sure your game can be quit

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False
    #draw the game
    display_surface.fill("cyan")
    pygame.display.update() #updates the whole window


pygame.quit()