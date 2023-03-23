import pygame
import os
from datetime import datetime
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("MickeyClock")
_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        _path = path.replace( '/' , os.sep).replace('\\', os.sep)
        image = pygame.image.load(_path)
        _image_library[path] = image
    return image


pos = (400, 400)

angle = 0
angle2 = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    mickey = get_image('mickeyclock.png')
    lefthand = get_image('lefthand.png')
    righthand = get_image('righthand.png')
    mickey = pygame.transform.scale(mickey,(600,600))
    lefthand = pygame.transform.scale(lefthand,(400,400))
    righthand = pygame.transform.scale(righthand,(400,400))
    rotated_image = pygame.transform.rotate(lefthand, angle)
    rotated_image2 = pygame.transform.rotate(righthand, angle2)
    angle -= 0.086
    angle2 -= 0.0023

    w, h = lefthand.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    origin = (pos[0] + min_box[0], pos[1] - max_box[1])

    w2, h2 = righthand.get_size()
    box2 = [pygame.math.Vector2(p) for p in [(0, 0), (w2, 0), (w2, -h2), (0, -h2)]]
    box_rotate2 = [p.rotate(angle2) for p in box2]
    min_box2 = (min(box_rotate2, key=lambda p: p[0])[0], min(box_rotate2, key=lambda p: p[1])[1])
    max_box2 = (max(box_rotate2, key=lambda p: p[0])[0], max(box_rotate2, key=lambda p: p[1])[1])

    origin2 = (pos[0] + min_box2[0], pos[1] - max_box2[1])

    screen.fill((255,255,255))

    rotated_image = pygame.transform.rotate(lefthand, angle)
    screen.blit(mickey, (120,120))
    rotated_image2 = pygame.transform.rotate(righthand, angle2)
    screen.blit(rotated_image, origin)
    screen.blit(rotated_image2, origin2)
    
    pygame.draw.ellipse(screen,(0,0,0),(375,385,35,35))

    pygame.display.flip()

pygame.quit()
