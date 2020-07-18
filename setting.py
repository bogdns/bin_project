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
FONT_DEATH = ('comicsansms', 32)
FONT_MENU = ('ubuntu', 42)
DIST_BETWEEN = WIDTH // ROWS
