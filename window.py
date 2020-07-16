import pygame


class Window:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.run = True  # flag, which show, what game is run / stop
        self.numberOfLines = 20  # number of horizontal / vertical lines
        self.distanceBetween = self.width // self.numberOfLines
        self.window = pygame.display.set_mode((self.width, self.height))  # main window of game


    def start_window(self):
        pygame.display.set_caption("Snail the game")  # title game

        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()