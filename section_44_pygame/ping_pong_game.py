import pygame, sys
from pygame.locals import *
import random

pygame.init()

size = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pend1 = 15
pend2 = 90

player_one_location_x = 50
player_one_location_y = 300 - 45
player_one_speed = 0

player_two_location_x = 700 - pend1
player_two_location_y = 300 - 45
player_two_speed = 0

ball = 0
ball_location_x = 400
ball_location_y = 300
ball_speed_x = 3
ball_speed_y = 3

time = pygame.time.Clock()

window = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[K_w]:
                player_one_speed = -3
            if keys[K_s]:
                player_one_speed = 3

            if keys[K_UP]:
                player_two_speed = -3
            if keys[K_DOWN]:
                player_two_speed = 3

        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()

            if keys[K_w]:
                player_one_speed = 0
            if keys[K_s]:
                player_one_speed = 0

            if keys[K_UP]:
                player_two_speed = 0
            if keys[K_DOWN]:
                player_two_speed = 0

    if ball_location_y > 590 or ball_location_y < 10:
        ball_speed_y *= -1

    if ball_location_x > 800 or ball_location_x < 0:
        ball_location_x = 400
        ball_location_y = 300
        ball_speed_x *= -1
        ball_speed_y *= -1

    player_one_location_y += player_one_speed
    player_two_location_y += player_two_speed

    if player_one_location_y > 600 or player_one_location_y < (0 - pend2):
        player_one_speed *= -1

    if player_two_location_y > 600 or player_two_location_y < (0 - pend2):
        player_two_speed *= -1

    ball_location_x += ball_speed_x
    ball_location_y += ball_speed_y

    window.fill(BLACK)

    player_one = pygame.draw.rect(window, WHITE, (player_one_location_x, player_one_location_y, pend1, pend2))
    player_two = pygame.draw.rect(window, WHITE, (player_two_location_x, player_two_location_y, pend1, pend2))
    ball = pygame.draw.circle(window, WHITE, (ball_location_x, ball_location_y), 10)

    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed_x *= -1

    pygame.display.flip()
    time.tick(60)
