from snake import *
import pygame as pg
from death import *
from food import *
import sys


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")
        icon = pg.image.load("snake.png")
        pg.display.set_icon(icon)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.distanceBetween = WIDTH // ROWS
        self.snake = Snake(self.window)
        self.clock = pg.time.Clock()
        self.menu = True  # for menu: false - not working menu; true - working menu
        self.gameb = False  # for game: false - not working game; true - working game
        self.death = False  # for snake: false - not death; true - snake death
        self.font = pg.font.SysFont('ubuntu', 42)  # fonts
        self.Death = Death(self.snake.pos, self.window, self.death)
        self.food = Food(self.window)

    def draw_matrix(self):
        """
        method for making matrix
        """
        matrix_x = 0
        matrix_y = 0
        for i in range(ROWS):
            matrix_x += self.distanceBetween
            matrix_y += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (matrix_x, 0), (matrix_y, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, matrix_y), (WIDTH, matrix_y))

    def main_menu(self):
        """
        launch main menu method
        """
        while self.menu:
            self.clock.tick(24)
            self.menu_update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
            pg.display.update()

    def game(self):
        """
        launch game method
        """
        while self.gameb:
            self.clock.tick(10)
            self.window.fill((0, 0, 0))
            self.draw_matrix()
            self.snake.update(self.food.ate)
            self.food.update(self.snake.pos)
            self.death = self.Death.field_check()  # checking snake death
            if self.death:
                self.menu = True  # menu open
                self.gameb = False  # game close
                self.snake.spawn()
                self.food.calculate_pos(self.snake.pos)
                self.food.update(self.snake.pos)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    exit()

            pg.display.update()

    def update_display(self):
        """
        method for running all windows, which we need to open
        """
        while True:
            self.main_menu()
            self.game()

    def menu_update(self):
        configs_menu = (self.window, (0, 90, 0), ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))
        """
        method updating menu icons and text 
        """
        self.window.fill((0, 150, 0))

        main_text = self.font.render("Snake game", 1, (0, 255, 0), (255, 255, 255))
        play_text = self.font.render("Play", 1, (255, 0, 0))

        mouse = pg.mouse.get_pos()  # using cordinates of mouse of player
        click = pg.mouse.get_pressed()  # using click check of mouse of player

        if ((WIDTH - 100) // 2 <= mouse[0] <= ((WIDTH - 100) // 2 + 100)) and ((HEIGHT - 50) // 2 <=
                                                                               mouse[1] <= ((HEIGHT - 50) // 2 + 50)):
            # pg.draw.rect(self.window, (0, 255, 0), ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))
            configs_menu = (self.window, (0, 255, 0), ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))
            if click[0] == 1:
                self.menu = False  # menu close
                self.death = False  # death snake is turning off
                self.gameb = True  # open the game

        pg.draw.rect(*configs_menu)
        self.window.blit(main_text, ((WIDTH - 170) // 2, HEIGHT // 4))
        self.window.blit(play_text, ((WIDTH - 100) // 2, (HEIGHT - 50) // 2))
