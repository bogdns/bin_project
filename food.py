from random import randint
from setting import *
import pygame as pg


class Food:
    def __init__(self, window):
        self.pos = (0, 0)  # init pos of a food
        self.distanceBetween = WIDTH // ROWS
        self.screen = window

    def calculate_pos(self, snake_pos):
        pass
        """
        calculates position of a food
        """

        return cords  # return position. cortege

    def draw_food(self, snake_pos):
        """
        spawns like cells of the snake
        """
        pg.draw.rect(self.screen, (0, 255, 0),
                     (self.calculate_pos(snake_pos), self.distanceBetween, self.distanceBetween))

    def update(self, snake_pos):
        """
        spawns food with library randint
        gets deque with positions of the snake and returns pos of the food
        """
        self.draw_food(snake_pos)
        # TODO
