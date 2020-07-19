import pygame as pg
import time
from quit_game import quit
pg.init()
# screen = pg.display.set_mode((700, 700))
from setting import *

while True:
    a = int(input())
    if a == 1:
        sounds = pg.mixer.Sound(VICTORY_SOUNDS[0][0])
        sounds.set_volume(VICTORY_SOUNDS[0][1])
        sounds.play()
    elif a == 2:
        sounds = pg.mixer.Sound(VICTORY_SOUNDS[1][0])
        sounds.set_volume(VICTORY_SOUNDS[1][1])
        sounds.play()
    elif a == 3:
        sounds = pg.mixer.Sound(VICTORY_SOUNDS[1][0])
        sounds.set_volume(VICTORY_SOUNDS[1][1])
        sounds.play()
# result_text = pg.font.SysFont(*FONT_VICTORY).render("VICTORY! BEER?", 1, COLOR_VICTORY)
#
# while True:
#     CLOCK.tick(10)
#     screen.blit(result_text, (WIDTH // 20, WIDTH // 4))
#     quit()
#     pg.display.update()