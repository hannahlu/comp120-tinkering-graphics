import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()

width = 1075
height = 788

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Teamwork')


black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
image = False
snapImg = pygame.image.load('headsnap.jpg')
font = pygame.font.SysFont('Serif', 90)
text = font.render('text here', True, (255, 255, 255))
text2 = font.render('text here', True, (255, 255, 255))

def spyro(x, y):
    window.blit(snapImg, (x, y))
    window.blit(text, (20, 10))
    window.blit(text2, (60, 100))

x = (0)
y = (0)

while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image = True

    window.fill(white)
    spyro(x, y)

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()
