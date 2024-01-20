import pygame, sys
from pygame.locals import *
import random

pygame.init()

tamaño = (800, 600)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

jug_ancho = 15
jug_alto = 90

jug1_co_x = 50
jug1_co_y = 300 - 45
jug1_vel_y = 0

jug2_co_x = 750 - jug_ancho
jug2_co_y = 300 - 45
jug2_vel_y = 0

pelota = 0
pelota_x = 400
pelota_y = 300
pelota_vel_x = 3
pelota_vel_y = 3

tiempo = pygame.time.Clock()

pantalla = pygame.display.set_mode(tamaño)
pygame.display.set_caption("Mi segundo videojuego")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[K_w]:
                jug1_vel_y = -3
            if keys[K_s]:
                jug1_vel_y = 3

            if keys[K_UP]:
                jug2_vel_y = -3
            if keys[K_DOWN]:
                jug2_vel_y = 3

        if evento.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()

            if keys[K_w]:
                jug1_vel_y = 0
            if keys[K_s]:
                jug1_vel_y = 0

            if keys[K_UP]:
                jug2_vel_y = 0
            if keys[K_DOWN]:
                jug2_vel_y = 0

    if pelota_y > 590 or pelota_y < 10:
        pelota_vel_y *= -1

    if pelota_x > 800 or pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        pelota_vel_x *= -1
        pelota_vel_y *= -1

    jug1_co_y += jug1_vel_y
    jug2_co_y += jug2_vel_y

    if jug1_co_y > 600 or jug1_co_y < (0 - jug_alto):
        jug1_vel_y *= -1

    if jug2_co_y > 600 or jug2_co_y < (0 - jug_alto):
        jug2_vel_y *= -1

    pelota_x += pelota_vel_x
    pelota_y += pelota_vel_y

    pantalla.fill(NEGRO)

    jugador1 = pygame.draw.rect(pantalla, BLANCO, (jug1_co_x, jug1_co_y, jug_ancho, jug_alto))
    jugador2 = pygame.draw.rect(pantalla, BLANCO, (jug2_co_x, jug2_co_y, jug_ancho, jug_alto))
    pelota = pygame.draw.circle(pantalla, BLANCO, (pelota_x, pelota_y), 10)

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_vel_x *= -1

    pygame.display.flip()
    tiempo.tick(60)  # normal juegos
