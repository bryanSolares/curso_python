import pygame, sys
from pygame.locals import *
import random

size = (800, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Game 1")

black = (0, 0, 0)
white = (255, 255, 255)
red = (220, 20, 60)
blue = (0, 0, 255)
green = (127, 255, 0)
yellow = (255, 215, 0)
pink = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                window.fill(white)
            if keys[K_y]:
                window.fill(yellow)
            if keys[K_b]:
                window.fill(blue)

    # window.fill(black)

    pygame.display.flip()
