from bogdan_project.snake import *
from bogdan_project.food import *
import sys


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")
        icon = pg.image.load("snake.png")
        pg.display.set_icon(icon)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.distanceBetween = WIDTH // ROWS
        self.snake = Snake(self.window)
        self.food = Food(self.window)

    def draw_matrix(self):
        matrix_x = 0
        matrix_y = 0
        for i in range(ROWS):
            matrix_x += self.distanceBetween
            matrix_y += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (matrix_x, 0), (matrix_y, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, matrix_y), (WIDTH, matrix_y))

    def update(self):
        run = True
        while run:
            pg.time.delay(100)
            self.window.fill((0, 0, 0)),
            self.draw_matrix()
            self.snake.update(self.food.ate)
            self.food.update(self.snake.pos)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)

            pg.display.update()
