from collections import deque
from setting import *
import pygame as pg


class Snake:
    def __init__(self, window):
        """
        direction: top - 1, down - 2, right - 3, left - 4
        """
        self.window = window
        self.direction = 1
        self.pos = deque()  # positions of the snake(what cells is it on)
        self.distanceBetween = WIDTH // ROWS
        self.center = (ROWS // 2) * self.distanceBetween
        self.pos.append((self.center, self.center))  # places head of the snake in the center

    def draw_green_cell(self, cords):
        pg.draw.rect(self.window, (0, 255, 0), (*cords, self.distanceBetween, self.distanceBetween))

    def draw_snake(self):
        for cords in self.pos:
            self.draw_green_cell(cords)

    def update(self):
        """
        moves snake
        """
