# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init() #initializes pygame, needed for things to run properly
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #defines window w/ size and such
clock = pygame.time.Clock() #clock
running = True #bool that makes sure your game can be quit
dt = 0 #deltaTime

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #this places the sprite in the middle of the screen

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False

    #draw the game

    # fill the screen with a color to wipe away anything from last frame
    display_surface.fill("red")

    # pygame.draw.circle(screen, "purple", player_pos, 40)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # takes all the elements in the while loop and draws them
    pygame.display.update() #updates the whole window
    # pygame.display.flip() #can only update part of the window

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()