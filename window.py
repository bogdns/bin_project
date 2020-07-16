import pygame
from snake import *


class Window:
    def __init__(self, width, height, window):
        self.window = window
        self.width = width
        self.height = height
        self.run = True  # flag, which show, what game is run / stop
        self.numberOfLines = 20  # number of horizontal / vertical lines
        self.distanceBetween = self.width // self.numberOfLines
        self.snake = Znake(self.distanceBetween, self.width, self.window)

    def start_window(self):

        pygame.display.set_caption("Snail the game")  # title game

        while self.run:
            pygame.time.delay(50)
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

            self.snake.spawn(self.width)
            pygame.display.update()

    def draw_matrix(self):

