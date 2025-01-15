# Example file showing a circle moving on screen
import pygame
from os.path import join

# pygame setup
pygame.init() #initializes pygame, needed for things to run properly
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption("Space Shooter by Tripothy")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #defines window w/ size and such
clock = pygame.time.Clock() #clock
running = True #bool that makes sure your game can be quit

#plain surface 
surf = pygame.Surface((100,200))
surf.fill("red")
x=100

#importing an image
path = join('..', 'images', 'player.png')
print(path)
player_surf = pygame.image.load(path).convert_alpha()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

    #draw the game
    display_surface.fill("darkgray")
    x += .1
    display_surface.blit(surf, (150,150))
    display_surface.blit(player_surf, (x,100))

    pygame.display.update() #updates the whole window

pygame.quit()