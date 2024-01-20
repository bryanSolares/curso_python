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

location_x = 100
location_y = 100
speed_x = 0
speed_y = 0

time = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            location_x -= 10

        if keys[K_RIGHT]:
            location_x += 10

        if keys[K_UP]:
            location_y -= 10

        if keys[K_DOWN]:
            location_y += 10


    window.fill(black)

    pygame.draw.circle(window, white, (location_x, location_y), 50)

    pygame.display.flip()
    time.tick(60)
