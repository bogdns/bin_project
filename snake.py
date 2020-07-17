from collections import deque
from setting import *
import pygame as pg


class Snake:
    def __init__(self, window):
        self.pos = deque()  # positions of the snake(what cells is it on)
        self.spawn()
        self.window = window
        self.direction_x = 0
        self.direction_y = -1
        self.distanceBetween = WIDTH // ROWS
        self.tail = self.pos[0]

    def spawn(self):
        self.pos.clear()
        self.pos.append((ROWS // 2, ROWS // 2))  # places head of the snake in the center
        self.pos.append((ROWS // 2, ROWS // 2 - 1))  # places body of the snake in the center

    def draw_green_cell(self, cords):
        pg.draw.rect(self.window, COLOR_GROUND, (*cords, self.distanceBetween, self.distanceBetween))

    def update(self, ate):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT] and self.direction_x != -1:
            self.direction_x = 1
            self.direction_y = 0
        elif key[pg.K_LEFT] and self.direction_x != 1:
            self.direction_x = -1
            self.direction_y = 0
        elif key[pg.K_UP] and self.direction_y != 1:
            self.direction_y = -1
            self.direction_x = 0
        elif key[pg.K_DOWN] and self.direction_y != -1:
            self.direction_y = 1
            self.direction_x = 0
        if ate:
            self.pos.appendleft(self.tail)

        self.pos.append((self.pos[-1][0] + self.direction_x,
                         self.pos[-1][1] + self.direction_y))

        self.tail = self.pos.popleft()

        for cords in self.pos:
            x = cords[0]
            y = cords[1]
            self.draw_green_cell((x * self.distanceBetween, y * self.distanceBetween))
