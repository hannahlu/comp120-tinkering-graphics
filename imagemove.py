import pygame, sys
import os
from pygame.locals import *

window_width = 900
window_height = 800
black = (0, 0, 0)
white = (255, 255, 255)

class Frog(object):
    def __init__(self):
        self.image = pygame.image.load('smallfrog.png')
        self.x = 500
        self.y = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        if key[pygame.K_LEFT]:
            self.x -= dist
        if key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Frog')

frog = Frog()
clock = pygame.time.Clock()

frogmove = True
while frogmove:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        frogmove = False

    frog.handle_keys()

    window.fill(white)
    frog.draw(window)
    pygame.display.update()

    clock.tick(40)

pygame.quit()
quit()
