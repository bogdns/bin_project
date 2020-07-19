# There is setting for game
import pygame as pg
from quit_game import quit

RESOLUTION = (WIDTH, HEIGHT) = (700, 700)  # resolution
ROWS = 20  # number of horizontal / vertical lines
FPS = 10

CLOCK = pg.time.Clock()

COLOR_SNAKE = (0, 255, 0)
COLOR_GROUND = (0, 0, 0)
COLOR_LINE = (255, 255, 255)
COLOR_FOOD = (255, 0, 0)
COLOR_MENU = (0, 150, 0)
COLOR_PLAY = (255, 0, 0)
COLOR_SETTINGS = (255, 0, 0)
COLOR_SNAKE_GAME = (0, 255, 0)
COLOR_UNPRESSED_MENU = (0, 90, 0)
COLOR_PRESSED_MENU = (0, 255, 0)
COLOR_GAME_OVER = (255, 255, 255)
COLOR_GAME_OVER_BACK = (0, 0, 0)
COLOR_VICTORY = (255, 255, 0)

TEXT_SIZE = HEIGHT // 15
FONT_DEATH = ('comicsansms', TEXT_SIZE)
FONT_MENU = ('ubuntu', TEXT_SIZE)
FONT_VICTORY = ('ubuntu', HEIGHT//8)
FONT_SETTINGS = ('ubuntu', TEXT_SIZE)
DIST_BETWEEN = WIDTH // ROWS

ROFL_MODE = True

if ROFL_MODE:
    DEFEAT_SOUNDS = (("sounds/defeat_rofl_1.ogg", 0.4), ("sounds/defeat_rofl_2.ogg", 0.3))
    VICTORY_SOUNDS = (("sounds/victory_rofl_1.ogg", 0.4),0)
    DEFEAT_PHOTOS = ("photos/defeat_rofl_1.jpg", "photos/defeat_rofl_2.jpg", "photos/defeat_rofl_3.jpg")
    VICTORY_PHOTOS = ("photos/victory_rofl_1.jpg", "photos/victory_rofl_2.jpg", "photos/victory_rofl_3.jpg")
else:
    DEFEAT_SOUNDS = (("sounds/defeat_1.ogg", 0.5), ("sounds/defeat_2.ogg", 0.3))
    VICTORY_SOUNDS = (("sounds/victory_1.ogg", 0.4), ("sounds/victory_2.ogg", 0.1))

FOOD_SOUND = pg.mixer.Sound('sounds/eat_food.ogg')
FOOD_SOUND.set_volume(1)

WIDTH4 = WIDTH // 4
WIDTH8 = WIDTH // 8
HEIGHT4 = HEIGHT // 4
HEIGHT8 = HEIGHT // 8
