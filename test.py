import pygame as pg
from random import choice
from quit_game import quit

pg.init()
from setting import *

window = pg.display.set_mode((400, 400))

while True:
    CLOCK.tick(24)
    victory_photo = pg.image.load(choice(VICTORY_PHOTOS)).convert()
    victory_photo = pg.transform.scale(victory_photo, (400, 400))
    window.blit(victory_photo, (0, 0))
    quit()
    pg.display.update()
