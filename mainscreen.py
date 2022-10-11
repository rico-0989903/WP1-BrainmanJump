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


class Button():
    def _init_(self,x,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(100, 200, start_image)
exit_button = Button(450, 200, exit_img)



run = True 
while run:

    screen.fill((0,0,0))

    start_button.draw()
    exit_button.draw()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()
