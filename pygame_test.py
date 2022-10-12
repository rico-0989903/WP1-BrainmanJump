import pygame
import random

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

# images
platform_image = pygame.image.load('Assets/Platforms.png').convert_alpha()

# classes
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# platform group
platform_group = pygame.sprite.Group()

# temp platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(70, 80)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * 100
    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)

# game loop
run = True
while run:

    # set framerate
    clock.tick(FPS)

    # set background color
    screen.fill((255, 255, 255))

    # drawing
    platform_group.draw(screen)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()
