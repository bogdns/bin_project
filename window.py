import setting
import pygame as pg


class Window:
    def __init__(self):
        pg.init()
        pg.display.set_caption("SNAKE")
        ico = pg.image.load("snake.png")
        pg.display.set_icon(ico)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen = pg.display.set_mode((setting.WIDTH, setting.HEIGHT))
        self.distanceBetween = WIDTH // ROWS

    def create_matrix(self):
        x = 0
        y = 0
        for i in range(ROWS):
            x += self.distanceBetween
            y += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (x, 0), (x, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, y), (WIDTH, y))

    def update(self):
        self.create_matrix()
        # TODO
