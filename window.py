from setting import *
import pygame as pg
from snake import *


class Window:
    def __init__(self):
        pg.init()
        pg.display.set_caption("SNAKE")
        ico = pg.image.load("snake.png")
        pg.display.set_icon(ico)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.distanceBetween = WIDTH // ROWS
        self.snake = Snake(self.window)
    def create_matrix(self):
        x = 0
        y = 0
        for i in range(ROWS):
            x += self.distanceBetween
            y += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (x, 0), (x, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, y), (WIDTH, y))

    def update(self):
        run = True
        while run:
            pg.time.delay(50)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.create_matrix()
            self.snake.draw_snake()
            pg.display.update()
