import pygame, sys # d and c separately
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()

#Sounds
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3 #for enemy
SPEED2 = 3 #for coin
SPEED3 = 2 #for diamond
SCORE = 0 #for enemy
SCORE2 = 0 #for coin
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)


background = pygame.image.load("images\AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self): #creating function for moving enemy's car
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        
        self.image = pygame.image.load("images\Coin.png")
        self.rect = self.image.get_rect()
        self.q = random.randint(40, SCREEN_WIDTH-40)
        self.q1 = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):     #creating function for moving coins
        self.rect.move_ip(0, SPEED2)
        if (self.rect.top > 422):
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 4), 1)

class diamond(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        
        self.image = pygame.image.load("images\diamond.png")
        r = 40
        t = 30
        self.image = pygame.transform.scale(self.image,(r,t))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):   #creating function for moving diamonds
        # global SCORE2
        # r = random.randint(10,50)
        # self.image = pygame.transform.scale(self.image,(r,r))
        self.rect.move_ip(0,SPEED3)
        if (self.rect.top > 444):
            # SCORE2 +=0 
            # self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 4), 1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self): #creating function for moving players's car
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
    
#Setting up Sprites        
P1 = Player()  #P1 = Player() class
E1 = Enemy()   
C1 = coin()
D1 = diamond()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

diamonds= pygame.sprite.Group()
diamonds.add(D1)

coins = pygame.sprite.Group()
coins.add(C1)

ewe = pygame.sprite.Group()
ewe.add(P1)

all_sprites = pygame.sprite.Group()

all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(D1)
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #       SPEED += 0.5     
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("D:"+str(SCORE), True, BLACK)
    scores2 = font_small.render("C:"+ str(SCORE2), True, BLACK)
    DISPLAYSURF.blit(scores, (360,5))   #diamonds will show up at the right corner above the coins
    DISPLAYSURF.blit(scores2, (360,25)) #coins will show up at the right corner below the diamonds
    
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, diamonds):
        SCORE += 2    #to add +2 for every diamond achieved
        count = 0
    if pygame.sprite.spritecollideany(P1, coins): 
        SCORE2 += 1 #to add +1 score for every coin achieved
        continue
    if SCORE2 >= 5:
        SPEED = 5
    if SCORE2 >= 10:
        SPEED = 8
    if SCORE2 >= 20:
        SPEED = 12
    if SCORE2 >= 30:
        SPEED = 30
        SPEED2 = 10
        SPEED3 = 8
    
    game_over = font.render("Game Over!", True, BLACK)
    game_over1 = font.render("Your Score: "+  str(SCORE2), True, BLACK)

    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (80,200))   #game_over, location for it
        DISPLAYSURF.blit(game_over1, (80, 300)) #game_over1, location for it
       
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()

        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2) #game over window will show up for 2 seconds
        pygame.quit()
        sys.exit()        
         
    pygame.display.update() #refresh game screen
    FramePerSec.tick(FPS)