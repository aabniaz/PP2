import pygame, sys #2.py
from pygame.locals import *
import random, time

snake_speed = 10

window_x = 720  #window size
window_y = 480

black = pygame.Color(0, 0, 0)   #colour definition
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()   #initialising

pygame.display.set_caption('Snake')    #Initialising the game window
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()   #FPS (frames per second) controller

snake_position = [100, 50]  # Define the default position of the snake

snake_body = [[100, 50],    # defining the first 4 blocks of the snake's body
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (window_x // 10)) * 10,   # fruit position
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

direction = 'RIGHT' # direction is to the right
change_to = direction

score = 0   # initial values
level = 0
x = 0

def show_score(choice, color, font, size):  # function for Score
    score_font = pygame.font.SysFont(font, size)    #creating a score_font font object
    score_surface = score_font.render('Score: ' + str(score), True, color) #creating a display surface object
    score_rect = score_surface.get_rect()   #create font object score_font
    game_window.blit(score_surface, score_rect) #display text

def show_level(choice, color, font, size): # function for levels
    score_font = pygame.font.SysFont(font, size)    #create a score_font font object
    score_surface = score_font.render('Level : ' + str(level), True, color)
    score_rect = score_surface.get_rect(topright=(650,0))
    game_window.blit(score_surface, score_rect)

def game_over() : ## game over function
    my_font = pygame.font.SysFont('algerian', 30) # creating font object my_font
    game_over1_surface = my_font.render('Game Over!', True, red)
    game_over_surface = my_font.render( # creating a text surface on which text
        'Your Score is: ' + str(score)+' Level: ' + str(level), True, red)
    game_over1_rect = game_over_surface.get_rect()
    game_over_rect = game_over1_surface.get_rect()
    game_over1_rect.midtop = ((400,100))
    game_over_rect.midtop = (window_x / 3, window_y / 3)    #text position 
    game_window.blit(game_over1_surface, game_over1_rect)
    game_window.blit(game_over_surface, game_over_rect) # blit will draw text on the screen
    pygame.display.flip()
    pygame.display.update()
         
    time.sleep(5)
    pygame.quit()
    quit()


# Main Function
while True :
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'

# If two keys are pressed at the same time we don't want the snake to split into two directions at the same time
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'

    if direction == 'UP' :  # Moving the snake
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10

# A snake's body growth mechanism,if fruit and snakes collide, points will be increased by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] :
        score += 1
        fruit_spawn = False
    else :
        snake_body.pop()

    if not fruit_spawn :
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)
    
    if score==x+40:
        snake_speed+=5
        level+=1
        x+=40

    for pos in snake_body :
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x - 10 :  # Game Over conditions
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10 :
        game_over()

    for block in snake_body[1 :] :
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over()

    # displaying score and level countinuously
    show_score(1, white, 'algerian', 30)
    show_level(1, white, 'algerian', 30)

    pygame.display.update()

    fps.tick(snake_speed)