import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()

# Player variables
SPEED = 1

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

    def draw(self):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def MoveRight(self):
        #TODO move position to right
        self.postion[0] += SPEED

    def MoveLeft(self):
        #TODO move position to left
        self.position[0] -= SPEED

    def JumpUp(self):
        #TODO Jump mechanic
        self.position[1]

# game loop
run = True
brainman = Player(SCREEN_WIDTH // 2, SCREEN_HEIGT - 150)
while run:

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
