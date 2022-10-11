import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()
MAX_PLATFORMS = 10

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')


start_img = pygame.image.load('image/start.png').convert_alpha()
exit_img = pygame.image.load('image/exit.png').convert_alpha()
credits_img = pygame.image.load('image/credits.png').convert_alpha()


run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()
