import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')

# classes


# game loop
run = True
while run:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # set framerate
    clock.tick(FPS)
pygame.quit()
