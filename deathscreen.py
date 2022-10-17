import pygame
import os 
from os import system

pygame.init()
pygame.font.init()
# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()
MAX_PLATFORMS = 10
score = 0
highscore = 0
# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump Menu')

# Images in map
start_img = pygame.image.load('images/start.png').convert_alpha()
exit_img = pygame.image.load('images/exit.png').convert_alpha()
credits_img = pygame.image.load('images/credits.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        #images Height and width info
        #self.image = image
        self.scale = (200, 100)
        self.image = pygame.transform.scale(image, self.scale)
        
        width = self.image.get_width()
        height = self.image.get_width()
        
        # Image size
        #s

       # Images rectangle 
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
# Buttoon on screen
    def draw(self):
        action = False
        #cursor position on screen
        pos = pygame.mouse.get_pos()

        #Cursor coordinates
        #print(pos)

        #Mouse click Leftbutton:[0]
        mouse_buttons = pygame.mouse.get_pressed()

        if self.rect.collidepoint(pos):
            if mouse_buttons[0] and self.clicked == False:
                print("clicked")
                self.clicked = True
                action = True
        


        #draw buttons on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

start_button = Button(SCREEN_WIDTH// 2 - 100, 400, start_img, (200, 100))
exit_button = Button(SCREEN_WIDTH// 2 - 100, 550, exit_img, (200, 100))

scorefile = open("scores.txt", 'r')
strscore = scorefile.read()
score = int(strscore)

highscorefile = open("highscore.txt", 'r')
strhighscore = highscorefile.read()
print(strhighscore)
highscore = int(strhighscore)
highscorefile.close()


if score > highscore:
    highscore = score
    print(highscore)
    highscorefile = open("highscore.txt", 'w')
    highscorefile.write(str(highscore))
    highscorefile.close()

font = pygame.font.SysFont('Comic Sans', 80)  
scorefont = pygame.font.SysFont('Comic Sans', 50)  
text = font.render('Game Over', False, (255, 255, 255))
scoretext = scorefont.render(f'Score = {score}', False, (255, 255, 255))
highscoretext = scorefont.render(f'Highscore = {highscore}', False, (255, 255, 255))


print(score)

run = True 
system('taskkill /F /FI "WINDOWTITLE eq BrainJump" ')
while run:

    screen.fill((0,0,0))
    screen.blit(text, (40, 10))
    screen.blit(scoretext, (40, 100))
    screen.blit(highscoretext, (40, 200))
    start_button.draw()
    exit_button.draw()


    


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if start_button.draw() == True:
            os.system('python game.py')
            run = False
        if exit_button.draw() == True:
            run = False

    pygame.display.update()

pygame.quit()
