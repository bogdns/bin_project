from menu import *


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")
        icon = pg.image.load("snake.png")
        pg.display.set_icon(icon)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.in_menu = Menu(self.window)

    def update(self):
        """
        opens menu
        """
        while True:
            CLOCK.tick(24)
            self.in_menu.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit(0)
            pg.display.update()