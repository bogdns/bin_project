import pygame
from random import randrange


class Snake(object):
    def __init__(self, pos, len):
        pass


class Food(object):
    def __init__(self):
        pass


class Map(object):
    def __init__(self):
        pass


def makeMatrix(width, rows, window):
    sizeBtwn = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x += sizeBtwn
        y += sizeBtwn
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(window, (255, 255, 255), (0, y), (x, width))


def drawMatrix(display):
    display.fill((0,0,0))
    makeMatrix(width, rows, display)
    pygame.display.update()


def main():
    width = 500
    height = 500
    rows = 20 #number of rows
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake the game")
    clock = pygame.time.Clock()
    run = True
    while run:
        pygame.time.delay(50)
        clock.tick(10)
        drawMatrix(window)
main()