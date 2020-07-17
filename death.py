from setting import *
import pygame as pg


class Death:
    def __init__(self, pos, window, death):
        self.pos = pos
        self.window = window
        self.font = pg.font.SysFont('comicsansms', 32)
        self.death = death

    def field_check(self):
        headX = self.pos[-1][0]
        headY = self.pos[-1][1]
        if headX > ROWS or headX < 0 or headY > ROWS or headY < 0:
            self.window.fill((0, 0, 0))
            death_text = self.font.render("Game over", 1, (0, 0, 0), (255, 255, 255))
            self.window.blit(death_text, (50, 50))
            self.death = True
            return self.death