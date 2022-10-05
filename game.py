import pygame
import random

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()
MAX_PLATFORMS = 10

# Player variables
SPEED = 12
GRAVITY = 0.25
JUMP_STRENGTH = 2.5

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')

# images
platform_image = pygame.image.load('Assets/Platforms.png').convert_alpha()
brainman_sprite = pygame.image.load('Assets/BrainMan.png').convert_alpha()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# classes
class Player():

    def __init__(self, x, y):
        self.image = pygame.transform.scale(brainman_sprite, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.flip = False
        self.vel_y = 0
        self.dy = 0

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def MoveRight(self):
        self.rect.x += SPEED

    def MoveLeft(self):
        self.rect.x -= SPEED

    def JumpUp(self):
        self.dy = 0
        self.vel_y = -JUMP_STRENGTH


    def MoveCheck(self):
        #Left and Right controls
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.flip = False
            self.MoveLeft()
        if key[pygame.K_d]:
            self.flip = True
            self.MoveRight()

        self.vel_y += GRAVITY
        self.dy += self.vel_y
        self.rect.y += self.dy

        #Corrects border collision
        if self.rect.left - SPEED < 0:
            self.MoveRight()
        if self.rect.right + SPEED > SCREEN_WIDTH:
            self.MoveLeft()
        if self.rect.bottom + self.dy > SCREEN_HEIGT:
            self.JumpUp()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# platform group
platform_group = pygame.sprite.Group()

# start platform
start_platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGT - 20, 100)
platform_group.add(start_platform)

# temp platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(70, 80)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * 100
    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)


# game loop
run = True
brainman = Player(SCREEN_WIDTH // 2, SCREEN_HEIGT - 150)
while run:

    #set framerate
    clock.tick(FPS)

    #set background color
    screen.fill((WHITE))

    # drawing

    platform_group.draw(screen)

    brainman.draw()

    

    #movement set
    brainman.MoveCheck()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()
