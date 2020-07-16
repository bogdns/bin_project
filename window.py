from snake import *


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")
        icon = pg.image.load("snake.png")
        pg.display.set_icon(icon)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.distanceBetween = WIDTH // ROWS
        self.snake = Snake(self.window)

    def draw_matrix(self):
        matrixX = 0
        matrixY = 0
        for i in range(ROWS):
            matrixX += self.distanceBetween
            matrixY += self.distanceBetween
            pg.draw.line(self.window, (255, 255, 255), (matrixX, 0), (matrixY, HEIGHT))
            pg.draw.line(self.window, (255, 255, 255), (0, matrixY), (WIDTH, matrixY))

    def update(self):
        run = True
        while run:
            pg.time.delay(50)
            self.window.fill((0, 0, 0))
            self.draw_matrix()
            self.snake.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            pg.display.update()