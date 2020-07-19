import pygame as pg

pg.init()

from setting import *

while True:
    a = int(input())
    if a == 1:
        FOOD_SOUND.play()
    elif a == 2:
        DEFEAT_SOUND_1.play()
    elif a == 3:
        DEFEAT_SOUND_ROFL_1.play()
    elif a == 4:
        DEFEAT_SOUND_ROFL_2.play()
    elif a == 5:
        VICTORY_SOUND_ROFL_1.play()
