import pygame as pg
def quit():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)