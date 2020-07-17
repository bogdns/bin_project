from snake import *
import pygame as pg
from death import *


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")
        icon = pg.image.load("snake.png")
        pg.display.set_icon(icon)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.distanceBetween = WIDTH // ROWS
        self.snake = Snake(self.window)
        self.clock = pg.time.Clock()
        self.menu = True
        self.gameb = False
        self.death = False
        self.font = pg.font.SysFont('arial', 32)
        self.Death = Death(self.snake.pos, self.window, self.death)

    def draw_matrix(self):
        matrixX = 0
        matrixY = 0
        for i in range(ROWS):
            matrixX += self.distanceBetween
            matrixY += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (matrixX, 0), (matrixY, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, matrixY), (WIDTH, matrixY))

    def main_menu(self):
        while self.menu:
            self.window.fill((0, 150, 0))
            self.menu_update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    exit()
            pg.display.update()

    def game(self):
        while self.gameb:
            self.clock.tick(20)
            self.draw_matrix()
            self.snake.update()
            self.death = self.Death.field_check()
            if self.death is True:
                self.menu = True
                self.gameb = False
                self.snake.pos.clear()
                self.snake.pos.append((ROWS // 2, ROWS // 2))  # places head of the snake in the center
                self.snake.pos.append((ROWS // 2 + 1, ROWS // 2 + 1))  # places body of the snake in the center

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    exit()

            pg.display.update()
            self.window.fill((0, 0, 0))

    def update_display(self):
        while True:
            self.main_menu()
            self.game()

    def menu_update(self):
        main_text = self.font.render("Snake game", 1, (0, 255, 0), (255, 255, 255))
        play_text = self.font.render("Play", 1, (255, 0, 0), (255, 255, 255))

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        self.window.blit(main_text, ((WIDTH - 170) // 2, HEIGHT // 4))
        self.window.blit(play_text, ((WIDTH - 100) // 2, (HEIGHT - 50) // 2))
        pg.draw.rect(self.window, (0, 90, 0), ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))

        if (mouse[0] >= (WIDTH - 100) // 2) and (mouse[0] <= (WIDTH // 2)) and (mouse[1] >= ((HEIGHT - 50) // 2)) and (
                mouse[1] <= (HEIGHT // 2)):
            pg.draw.rect(self.window, (0, 255, 0), ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))
            if click[0] == 1:
                self.menu = False
                self.death = False
                self.gameb = True
