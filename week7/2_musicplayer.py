import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('My Playlist')

songs = ['music1.mp3','music2.mp3','music3.mp3']
order = 0
current = songs[order]
path = os.path.join('music', current)
pygame.mixer.music.load(path)

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        _path = path.replace( '/' , os.sep).replace('\\', os.sep)
        image = pygame.image.load(_path)
        _image_library[path] = image
    return image

pygame.mixer.music.play(0) 
def next(): 
    global order 
    global current 
    global songs 
    global path 
    order -=1 
    current=songs[order] 
    path=os.path.join("music",current) 
    pygame.mixer.music.load(path) 
    pygame.mixer.music.play(0) 

def previous(): 
        global order 
        global current 
        global songs 
        global path 
        order +=1 
        current=songs[order] 
        path=os.path.join("music",current) 
        pygame.mixer.music.load(path) 
        pygame.mixer.music.play(0) 

done=False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:  
                pygame.mixer.music.pause() 
            else:
                pygame.mixer.music.unpause()  
            if event.key == pygame.K_LEFT:  
                previous() 
            if event.key == pygame.K_RIGHT:  
                next()    
        image = get_image('music.png')
        image = pygame.transform.scale(image,(200,200))
        font = pygame.font.Font(None,50)
        text = font.render('My Playlist',True, (255,255,255))
        screen.blit(text,(100,30))
        screen.blit(image,(90,80))


    pygame.display.flip()