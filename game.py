import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()

# Player variables
SPEED = 5

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')

#images
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

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def MoveRight(self):
        self.rect.x += SPEED

    def MoveLeft(self):
        self.rect.x -= SPEED

    def JumpUp(self):
        #TODO Jump mechanic
        self.position[1]

    def MoveCheck(self):
        #Left and Right controls
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.flip = False
            self.MoveLeft()
        if key[pygame.K_d]:
            self.flip = True
            self.MoveRight()

        #Corrects border collision
        if self.rect.left - SPEED < 0:
            self.MoveRight()
        if self.rect.right + SPEED > SCREEN_WIDTH:
            self.MoveLeft()



# game loop
run = True
brainman = Player(SCREEN_WIDTH // 2, SCREEN_HEIGT - 150)
while run:

    #movement set
    brainman.MoveCheck()

    #set framerate
    clock.tick(FPS)

    #set background color
    screen.fill((WHITE))

    #Player
    brainman.draw()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
