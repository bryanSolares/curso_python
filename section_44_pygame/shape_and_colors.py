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
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # color
    window.fill(black)

    # draw
    pygame.draw.line(window, yellow, [50, 60], [30, 30], width=5)
    pygame.draw.rect(window, red, (100, 100, 250, 250))
    pygame.draw.circle(window, green, (400, 350), 50)

    for x in range(100, 1000, 100):
        pygame.draw.rect(window, yellow, (x - 50, 50, 50, 50))

    pygame.display.flip()
