from in_game import *
from settings_menu import *


class Menu:
    def __init__(self, window):
        self.screen = window

        self.game = Game(self.screen)
        self.settings = Settings()

        self.font = pg.font.SysFont(*FONT_MENU)
        self.main_text = self.font.render("Snake game", 1, COLOR_SNAKE_GAME)
        self.play_text = self.font.render("Play", 1, COLOR_PLAY)
        self.configs_menu = (self.screen, COLOR_UNPRESSED_MENU, ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))

    def draw_buttons(self, configs_menu):
        pg.draw.rect(*configs_menu)
        self.screen.blit(self.main_text, ((WIDTH - 170) // 2, HEIGHT // 4))
        self.screen.blit(self.play_text, ((WIDTH - 100) // 2, (HEIGHT - 50) // 2))

    def check_m_on_play(self, mouse, click):
        if ((WIDTH - 100) // 2 <= mouse[0] <= ((WIDTH - 100) // 2 + 100)) and ((HEIGHT - 50) // 2 <=
                                                                               mouse[1] <= ((HEIGHT - 50) // 2 + 50)):
            self.configs_menu = (self.screen, COLOR_PRESSED_MENU, ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))
            if click[0] == 1:
                self.game.start_game()

    def check_m_on_settings(self, mouse, click):
        pass

    def update(self):
        """
        method updating menu icons and text 
        """
        self.configs_menu = (self.screen, COLOR_UNPRESSED_MENU, ((WIDTH - 100) // 2, (HEIGHT - 50) // 2, 100, 50))
        self.screen.fill(COLOR_MENU)

        mouse = pg.mouse.get_pos()  # using cordinates of mouse of player
        click = pg.mouse.get_pressed()  # using click check of mouse of player

        self.check_m_on_play(mouse, click)
        self.check_m_on_settings(mouse, click)

        self.draw_buttons(self.configs_menu)
