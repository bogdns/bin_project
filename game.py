import pygame
from random import randrange
from snake import *

pygame.init()

x_coord = 0
y_coord = 0

x = 0
y = 0
length = 1

    if food == 0:
        x_coordf = (randrange(0, height) // lengBtwn) * lengBtwn
        y_coordf = (randrange(0, height) // lengBtwn) * lengBtwn
        # pygame.draw.rect(window, (0, 255, 0), (x_coord - (dirn_x*lengBtwn), y_coord - (dirn_y*lengBtwn), lengBtwn, lengBtwn))
        pygame.draw.rect(window, (255, 0, 0), (x_coordf, y_coordf, lengBtwn, lengBtwn))
        food = 1
    pygame.draw.rect(window, (255, 0, 0), (x_coordf, y_coordf, lengBtwn, lengBtwn))
    pygame.draw.rect(window, (0, 255, 0), (x_coord, y_coord, lengBtwn, lengBtwn))
    for i in range(rows):
        x += lengBtwn
        y += lengBtwn
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, height))
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))



    if x_coord == x_coordf and y_coord == y_coordf:
        length += 1
        food = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x = 0
    y = 0