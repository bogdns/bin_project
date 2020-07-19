from random import choice
from setting import *
import pygame as pg


class Food:
    def __init__(self, window):
        self.pos = (0, 0)  # init pos of a food
        self.distanceBetween = WIDTH // ROWS
        self.screen = window
        self.free_cells = set()  # cells which are free to place food
        for i in range(ROWS):
            for j in range(ROWS):
                self.free_cells.add((i, j))
        self.calculate_pos([(ROWS // 2, ROWS // 2), (ROWS // 2, ROWS // 2 - 1)])
        self.ate = 0
        self.score = 0

    def calculate_pos(self, snake_pos):
        """
        calculates position of a food
        """
        if len(snake_pos) == ROWS ** 2:
            self.cords = (-2, -2)
        else:
            self.cords = choice(list(self.free_cells.difference(set(snake_pos))))  # return position. cortege

    def draw_food(self):
        """
        spawns like cells of the snake
        """
        pg.draw.rect(self.screen, COLOR_FOOD,
                     (self.cords[0] * self.distanceBetween,
                      self.cords[1] * self.distanceBetween,
                      self.distanceBetween,
                      self.distanceBetween))

    def update(self, snake_pos):
        """
        spawns food with library randint
        gets deque with positions of the snake and returns pos of the food
        """
        self.ate = 0
        if snake_pos[-1] == self.cords:  # поедание еды
            FOOD_SOUND.play()
            self.calculate_pos(snake_pos)
            self.ate = 1
            self.score += 1
        self.draw_food()
