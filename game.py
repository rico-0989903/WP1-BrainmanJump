import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')

# game loop
run = True
while run:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
