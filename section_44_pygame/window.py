import pygame, sys
from pygame.locals import *
import random

size = (800, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Game 1")

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()