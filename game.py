import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

x = 400
y = 300

Col = False

Shrek = pygame.transform.scale(pygame.image.load('ShrekDV.png'),(80,100))
SynthF = pygame.transform.scale(pygame.image.load('SynthFont.jpg'),(800,600))
Test1 = pygame.Rect(400,400,420,420)
Test = pygame.Rect(500,500,510,610)
Colliders = [Test]

while True:
    screen.fill((0, 0, 0))
    #screen.blit(SynthF,(0,0))

    pygame.event.pump()
    if pygame.event.peek(pygame.QUIT):
        break
    
    if Test1.collidelist(Colliders) == -1:
        Col = True
    else:
        Col = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if Col == False:
            x -= 3

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if Col == False:
            x += 3

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_UP]:

    screen.blit(Shrek,(x,y))

    pygame.display.flip()
    time.sleep(1 / 60)
