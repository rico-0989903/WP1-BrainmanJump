from cmath import rect
from tkinter import scrolledtext
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
background_image = pygame.image.load('Assets/BG.png').convert_alpha()
platform_image = pygame.image.load('Assets/Platforms.png').convert_alpha()
brainman_sprite = pygame.image.load('Assets/BrainMan.png').convert_alpha()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# classes
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.moving = moving 
        self.move_counter = random.randint(70, 80)
        self.direction = random.choice([-2, 2])
        self.rect.x = x
        self.rect.y = y

def update(self,scroll):
    if self.moving == True:
        self.rect.x += self.direction 
        
    self.rect.y += scroll

    if self.rect.top > SCREEN_HEIGT:
        self.kill()


class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(brainman_sprite, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.flip = False
        self.vel_y = 0
        self.dy = 0
    
    # prints character on screen
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    # movement right
    def MoveRight(self):
        self.rect.x += SPEED

    # movent left
    def MoveLeft(self):
        self.rect.x -= SPEED

    # Jumping
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

        # side switch
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        
        # temp bottom screen collision
        if self.rect.bottom + self.dy > SCREEN_HEIGT:
            self.JumpUp()
        
        # platform collision
        for platform in platform_group:
            # checks if player is colliding with the platforms
            if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, 35, 35):
                # checks if player is above the platform
                if self.rect.bottom < platform.rect.centery:
                    # checks if player is falling down
                    if self.dy > 0:
                        # puts player flat on the platform for clean looks
                        self.rect.bottom = platform.rect.top
                        self.dy = 0
                        self.JumpUp()




# platform group
platform_group = pygame.sprite.Group()

# start platform
start_platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGT - 20, 100, False)
platform_group.add(start_platform)

# temp platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(70, 80)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * 100
    p_type = random.randint(1, 2)
    if p_type == 1:
        p_moving = True
    else: 
        p_moving =  False
    platform = Platform(p_x, p_y, p_w, p_moving)  
    platform_group.add(platform)


# game loop
run = True
brainman = Player(SCREEN_WIDTH // 2, SCREEN_HEIGT - 50)
while run:

    #set framerate
    clock.tick(FPS)

    

    # drawing
    screen.blit(background_image, (0, 0))

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
