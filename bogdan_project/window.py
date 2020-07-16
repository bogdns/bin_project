import setting
import pygame as pg


class Window:
    def __init__(self):
        pg.init()
        pg.display.set_caption("SNAKE")
        ico = pg.image.load("snake.png")
        pg.display.set_icon(ico)
        self.screen = pg.display.set_mode((setting.WIDTH, setting.HEIGHT))

    def create_matrix(self):
        pass

    def update(self):
        self.create_matrix()
        # TODO
