from bogdan_project.setting import *
import pygame as pg


class Death:
    def __init__(self, pos, window, death):
        self.pos = pos
        self.window = window
        self.font = pg.font.SysFont(*FONT_DEATH)
        self.death = death

    def field_check(self):
        head_x = self.pos[-1][0]
        head_y = self.pos[-1][1]
        if head_x > ROWS or head_x < 0 or head_y > ROWS or head_y < 0:
            self.window.fill(COLOR_GAME_OVER_BACK)
            death_text = self.font.render("Game over", 1, COLOR_GAME_OVER)
            self.window.blit(death_text, (50, 50))
            self.death = True
            return self.death
