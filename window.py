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
        x = 0
        y = 0
        for i in range(rows):
            x += lengBtwn
            y += lengBtwn
            pygame.draw.line(window, (255, 255, 255), (x, 0), (x, HEIGHT))
            pygame.draw.line(window, (255, 255, 255), (0, y), (WIDTH, y))
        

    def update(self):
        self.create_matrix()
        # TODO

