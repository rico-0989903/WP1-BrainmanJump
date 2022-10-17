import os
import random

import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()
MAX_PLATFORMS = 10

# Game variables
SPEED = 12
PLATFORM_SPACING = 120
SCROLL = SCREEN_HEIGT - PLATFORM_SPACING
GRAVITY = 0.25
JUMP_STRENGTH = 2.4
scrolled_dist = 0
background_scroll = 0

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

#Game functions
def scrollingbackground(background_scroll):
    screen.blit(background_image, (0, 0 + background_scroll))
    screen.blit(background_image, (0, -background_image.get_height() + background_scroll))



# classes
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        #Update platform positions when threshold is reached
        self.rect.y += scroll

        if self.rect.top > SCREEN_HEIGT - 10:
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
        scroll = 0

        if key[pygame.K_a]:
            self.flip = False
            self.MoveLeft()
        if key[pygame.K_d]:
            self.flip = True
            self.MoveRight()

        # side switch
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        
        # temp bottom screen collision
        if brainman.rect.top > SCREEN_HEIGT + 50:
            with open("scores.txt", 'w') as scorefile:
                scorefile.write(str(int(score)))
            os.system('python deathscreen.py')
            
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

        if self.rect.top <= SCROLL:
            if self.vel_y < 0:
                scroll = -self.dy

        self.vel_y += GRAVITY
        self.dy += self.vel_y
        self.rect.y += self.dy + scroll

        return scroll


# platform group
platform_group = pygame.sprite.Group()

# start platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGT - 30, 100)
platform_group.add(platform)

# score
score = 0
font = pygame.font.SysFont('Comic Sans', 50)
#text = font.render(f'Score: {score}', False, (255, 255, 255))

# game loop
run = True
brainman = Player(SCREEN_WIDTH // 2, SCREEN_HEIGT - 50)
os.system('taskkill /F /FI "WINDOWTITLE eq BrainJump Menu" ')
while run:
    #set framerate
    clock.tick(FPS)

    #checks player movement
    scroll = brainman.MoveCheck()
  
    # drawing
    background_scroll += scroll
    if background_scroll >= background_image.get_height():
        background_scroll = 0
    scrollingbackground(background_scroll)

    #score text
    text = font.render(f'Score: {int(score)}', False, (255, 255, 255))
    screen.blit(text, (10,0))

    #Platform generating
    if len(platform_group) < MAX_PLATFORMS:
        p_w = random.randint(70, 80)
        p_x = random.randint(0, SCREEN_WIDTH - p_w)
        p_y = platform.rect.y - PLATFORM_SPACING
        platform = Platform(p_x, p_y, p_w)
        platform_group.add(platform)
    

    #movement set
    platform_group.update(scroll)

    platform_group.draw(screen)
    brainman.draw()
    score = score + scroll
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    
    pygame.display.update()
pygame.quit()