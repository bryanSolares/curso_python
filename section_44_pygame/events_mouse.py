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

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    window.fill(black)

    location_mouse = pygame.mouse.get_pos()
    mouse_x = location_mouse[0]
    mouse_y = location_mouse[1]

    pygame.draw.circle(window, green, (mouse_x, mouse_y), 50)


    pygame.display.flip()
