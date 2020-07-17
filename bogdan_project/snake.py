from collections import deque
from bogdan_project.setting import *
import pygame as pg


class Snake:
    def __init__(self, window):
        self.window = window
        self.directionX = 0
        self.directionY = -1
        self.pos = deque()  # positions of the snake(what cells is it on)
        self.distanceBetween = WIDTH // ROWS
        self.pos.append((ROWS // 2, ROWS // 2))  # places head of the snake in the center
        self.pos.append((ROWS // 2, ROWS // 2 - 1))  # places body of the snake in the center
        self.tail = self.pos[0]

    def draw_green_cell(self, cords):
        pg.draw.rect(self.window, (0, 255, 0), (*cords,
                                                self.distanceBetween,
                                                self.distanceBetween))

    def update(self, ate):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            self.directionX = 1
            self.directionY = 0
        if key[pg.K_LEFT]:
            self.directionX = -1
            self.directionY = 0
        if key[pg.K_UP]:
            self.directionX = 0
            self.directionY = -1
        if key[pg.K_DOWN]:
            self.directionX = 0
            self.directionY = 1
        if ate:
            self.pos.appendleft(self.tail)
        self.pos.append((self.pos[-1][0] + self.directionX,
                         self.pos[-1][1] + self.directionY))
        self.tail = self.pos.popleft()

        for cords in self.pos:
            x = cords[0]
            y = cords[1]
            self.draw_green_cell((x * self.distanceBetween,
                                  y * self.distanceBetween))
