import pygame as pg
import sys

pg.init()
pg.display.set_caption("SNAKE")
ico = pg.image.load("snake.png")
pg.display.set_icon(ico)
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
    screen.fill((255, 255, 255))
    pg.draw.line(screen, (0, 0, 0), (10, 20), (100, 200), 10)
    pg.display.update()
    clock.tick(30)
