import pygame

pygame.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()

# Player variables
SPEED = 10
STARTING_POSITION = 120

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')

# classes
class Player(object):

    def __init__(self, position):
        #TODO set base position
        self.position = position

    def MoveRight(self):
        #TODO move position to right
        self.postion += SPEED

    def MoveLeft(self):
        #TODO move position to left
        self.position -= SPEED

# game loop
run = True
player = Player(STARTING_POSITION)
while run:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # set framerate
    clock.tick(FPS)
pygame.quit()
