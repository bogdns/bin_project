from snake import *
import pygame as pg
from death import *


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")
        icon = pg.image.load("snake.png")
        pg.display.set_icon(icon)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.distanceBetween = WIDTH // ROWS
        self.snake = Snake(self.window)
        self.clock = pg.time.Clock()
        self.run = True
        self.death = Death(self.snake.pos, self.window, self.run)

    def draw_matrix(self):
        matrixX = 0
        matrixY = 0
        for i in range(ROWS):
            matrixX += self.distanceBetween
            matrixY += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (matrixX, 0), (matrixY, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, matrixY), (WIDTH, matrixY))

    def update(self):
        while self.run:
            self.clock.tick(20)
            self.draw_matrix()
            self.snake.update()
            self.death.field_check()
            if self.death.death is True:
                self.run = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

            pg.display.update()
            self.window.fill((0, 0, 0))
