import os
import random

import pygame

pygame.init()
pygame.mixer.init()

# variables
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGT = 800
clock = pygame.time.Clock()
MAX_PLATFORMS = 10
MAIN_MENU = True
GAME_OVER = False
MAX_ENEMY = 1

# Game variables
SPEED = 12
PLATFORM_SPACING = 120
SCROLL = SCREEN_HEIGT - 200
GRAVITY = 0.25
JUMP_STRENGTH = 2.4
scrolled_dist = 0
background_scroll = 0

#Sound variables
jump_sound = pygame.mixer.Sound("sounds/jump.wav")
death_sound = pygame.mixer.music.load("sounds/death.mp3")

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('BrainJump')

# images
enemy_sprite = pygame.image.load('Assets/Enemy.png').convert_alpha()
background_image = pygame.image.load('Assets/BG.png').convert_alpha()
platform_image = pygame.image.load('Assets/Platforms.png').convert_alpha()
brainman_sprite = pygame.image.load('Assets/BrainMan.png').convert_alpha()
start_img = pygame.image.load('images/start.png').convert_alpha()
exit_img = pygame.image.load('images/exit.png').convert_alpha()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#GAME OVER MENU
#button class
class Buttondeath():
    def __init__(self, x, y, image, scale):
        #images Height and width info
        #self.image = image
        self.scale = (200, 100)
        self.image = pygame.transform.scale(image, self.scale)      
        width = self.image.get_width()
        height = self.image.get_width()     
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
# Buttoon on screen
    def draw(self):
        action = False
        #cursor position on screen
        pos = pygame.mouse.get_pos()
        #Mouse click Leftbutton:[0]
        mouse_buttons = pygame.mouse.get_pressed()

        if self.rect.collidepoint(pos):
            if mouse_buttons[0] and self.clicked == False:
                self.clicked = True
                action = True

      
            
        #draw buttons on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#buttons
deathstart_button = Buttondeath(SCREEN_WIDTH// 2 - 100, 400, start_img, (200, 100))
deathexit_button = Buttondeath(SCREEN_WIDTH// 2 - 100, 550, exit_img, (200, 100))

#MAIN MENU
#button class
class Button():
    def __init__(self, x, y, image, scale):
        #images Height and width info
        #self.image = image
        self.scale = (200, 100)
        self.image = pygame.transform.scale(image, self.scale)      
        width = self.image.get_width()
        height = self.image.get_width()     
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
# Buttoon on screen
    def draw(self):
        action = False
        #cursor position on screen
        pos = pygame.mouse.get_pos()
        #Mouse click Leftbutton:[0]
        mouse_buttons = pygame.mouse.get_pressed()

        if self.rect.collidepoint(pos):
            
            if mouse_buttons[0] and self.clicked == False:
                self.clicked = True
                action = True
        #draw buttons on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
   

#buttons
start_button = Button(SCREEN_WIDTH// 2 - 100, 300, start_img, (200, 100))
exit_button = Button(SCREEN_WIDTH// 2 - 100, 450, exit_img, (200, 100))

#main menu text
menufont = pygame.font.SysFont('Eras Bold ETC', 110)
text = menufont.render('Main Menu', False, (0, 0, 0))





#Game functions
def scrollingbackground(background_scroll):
    screen.blit(background_image, (0, 0 + background_scroll))
    screen.blit(background_image, (0, -background_image.get_height() + background_scroll))



# classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.direction = random.choice([-1, 1])
        self.image = pygame.transform.scale(enemy_sprite, (40, 40))
        self.rect = self.image.get_rect()
          
        if self.direction == 1:
            self.rect.x = 0
        else:
            self.rect.x = SCREEN_WIDTH
        self.rect.y = y

    def update(self, scroll):
        self.rect.y += scroll
        self.rect.x += self.direction * 2

        if self.direction == 1:
            if self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
        if self.direction == -1:
            if self.rect.right < 0:
                self.rect.left = SCREEN_HEIGT
        if self.rect.top > SCREEN_HEIGT - 10:
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, False), self.rect)

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
        pygame.mixer.Sound.play(jump_sound)
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

        self.mask = pygame.mask.from_surface(self.image)

        return scroll


# platform group
platform_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# start platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGT - 20, 100)
platform_group.add(platform)

# score
score = 0
font = pygame.font.SysFont('Comic Sans', 50)


#MAIN MENU DRAW



#GAME OVER MENU

highscorefile = open("highscore.txt", 'r')
strhighscore = highscorefile.read()
highscore = int(strhighscore)
highscorefile.close()




deathfont = pygame.font.SysFont('Eras Bold ETC', 110)  
scorefont = pygame.font.SysFont('Eras Demi ETC', 60)  
deathtext = deathfont.render('Game Over', False, (0, 0, 0))

PLAYER_MADE = False
# game loop
run = True
brainman = Player(SCREEN_WIDTH // 2, SCREEN_HEIGT - 50)


while run:
    clock.tick(FPS)
    if MAIN_MENU == True:
        screen.fill((255,210,210))
        screen.blit(text, (50, 50))
        pos = pygame.mouse.get_pos()
        if start_button.rect.collidepoint(pos):  
            pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(SCREEN_WIDTH// 2 - 95, 305, 210, 110))
        start_button.draw()
        if exit_button.rect.collidepoint(pos):  
            pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(SCREEN_WIDTH// 2 - 95, 455, 210, 110))
        exit_button.draw()
        #GAME ITSELF
    if MAIN_MENU == False and GAME_OVER == False:
        #checks player movement
        scroll = brainman.MoveCheck()
    
        # drawing
        background_scroll += scroll
        if background_scroll >= background_image.get_height():
            background_scroll = 0
        scrollingbackground(background_scroll)

        #score text
        text = font.render(f'Score: {int(score)}', False, (0, 0, 0))
        screen.blit(text, (10,0))

        #Platform generating
        if len(platform_group) < MAX_PLATFORMS:
            p_w = random.randint(70, 80)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - PLATFORM_SPACING
            platform = Platform(p_x, p_y, p_w)
            platform_group.add(platform)

        if len(enemy_group) == 0:
            enemy = Enemy(0)
            enemy_group.add(enemy)
        
        #movement set
        platform_group.update(scroll)
        platform_group.draw(screen)
        brainman.draw()
        
        score = score + scroll
        if brainman.rect.top > SCREEN_HEIGT + 50:
            pygame.mixer.music.play(death_sound)
            GAME_OVER = True

        if pygame.sprite.spritecollide(brainman, enemy_group, False): 
            if pygame.sprite.spritecollide(brainman, enemy_group, False, pygame.sprite.collide_mask):
            #for enemy in enemy_group:
            #   if enemy.rect.colliderect(brainman.rect.x, brainman.rect.y, 35, 35):
                    pygame.time.wait(500)
                    pygame.mixer.music.play(death_sound)
                    GAME_OVER = True

        if score > 2000:
            enemy_group.update(scroll)
            enemy_group.draw(screen)
            

    #GAME OVER MENU
    if GAME_OVER == True:
        
        enemy_group.empty()
        if score > highscore:
            highscore = int(score)
            print(highscore)
            highscorefile = open("highscore.txt", 'w')
            highscorefile.write(str(highscore))
            highscorefile.close()

        scoretext = scorefont.render(f'Score = {int(score)}', False, (0, 0, 0))
        highscoretext = scorefont.render(f'Highscore = {highscore}', False, (0, 0, 0))
        screen.fill((255,210,210))
        screen.blit(deathtext, (40, 40))
        screen.blit(scoretext, (40, 180))
        screen.blit(highscoretext, (40, 280))
        pos = pygame.mouse.get_pos()
        if deathstart_button.rect.collidepoint(pos):  
            pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(SCREEN_WIDTH// 2 - 95, 405, 210, 110))
        deathstart_button.draw()
        if deathexit_button.rect.collidepoint(pos):  
            pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(SCREEN_WIDTH// 2 - 95, 555, 210, 110))
        deathexit_button.draw()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if MAIN_MENU == True:
            if start_button.draw() == True:
                MAIN_MENU = False
            if exit_button.draw() == True:
                run = False
        if GAME_OVER == True:
            deathstart_button.clicked = False
            
            if deathstart_button.draw() == True:
                highscorefile = open("highscore.txt", 'r')
                strhighscore = highscorefile.read()
                highscore = int(strhighscore)
                highscorefile.close()
                score = 0
                scroll = 0
                brainman.dy = -20
                platform_group.empty()
                platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGT - 20, 100)
                platform_group.add(platform)
                brainman.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGT - 120)
                GAME_OVER = False
                
            if deathexit_button.draw() == True:
                run = False
        
    
    pygame.display.update()
pygame.quit()