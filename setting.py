# There is setting for game
import pygame as pg
from quit_game import quit

RESOLUTION = (WIDTH, HEIGHT) = (400, 400)  # resolution
ROWS = 20  # number of horizontal / vertical lines
FPS = 10

CLOCK = pg.time.Clock()

COLOR_SNAKE = (0, 255, 0)
COLOR_GROUND = (0, 0, 0)
COLOR_LINE = (255, 255, 255)
COLOR_FOOD = (255, 0, 0)
COLOR_MENU = (0, 150, 0)
COLOR_PLAY = (255, 0, 0)
COLOR_SNAKE_GAME = (0, 255, 0)
COLOR_UNPRESSED_MENU = (0, 90, 0)
COLOR_PRESSED_MENU = (0, 255, 0)
COLOR_GAME_OVER = (255, 255, 255)
COLOR_GAME_OVER_BACK = (0, 0, 0)
COLOR_VICTORY = (255, 255, 0)

FONT_DEATH = ('comicsansms', HEIGHT // 12)
FONT_MENU = ('ubuntu', HEIGHT // 9)
FONT_VICTORY = ('ubuntu', HEIGHT // 9)

DIST_BETWEEN = WIDTH // ROWS

WIDTH4 = WIDTH // 4
WIDTH8 = WIDTH // 8
HEIGHT4 = HEIGHT // 4
HEIGHT8 = HEIGHT // 8
