import pygame

pygame.init()
red = (255,0,0)
size =  (600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Red Ball')

x = 0
y = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 20
            if y <= 0:
                y = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y +=20
            if y >= 550:
                y = 550
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -=20
            if x <=0:
                x = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x +=20
            if x >=550:
                x = 550
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen, red,(x,y,50,50),100)

    pygame.display.update()

pygame.quit()