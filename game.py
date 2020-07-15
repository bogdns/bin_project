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


def main():
    width = 500
    height = 500
    x, y = randrange(0, width), randrange(0, width)
    length = 1
    snake = Snake((x, y), length)
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake the game")