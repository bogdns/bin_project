from in_game import *
from settings_menu import *


class Menu:
    def __init__(self, window):
        self.screen = window

        self.game = Game(self.screen)
        self.settings = Settings(self.screen)

        self.font = pg.font.SysFont(*FONT_MENU)
        self.main_text = self.font.render("Snake game", 1, COLOR_SNAKE_GAME)
        self.play_text = self.font.render("Play", 1, COLOR_PLAY)
        self.settings_text = self.font.render("Settings", 1, COLOR_SETTINGS)
        self.configs_menu = (self.screen, COLOR_UNPRESSED_MENU,
                             ((WIDTH - WIDTH4) // 2, (HEIGHT - HEIGHT8) // 2, WIDTH4, HEIGHT8))

    def draw_buttons(self, configs_menu):
        """
        shows buttons on the menu screen
        """
        self.screen.blit(self.main_text, ((WIDTH - WIDTH // 2.35) // 2, HEIGHT4))
        self.screen.blit(self.play_text, ((WIDTH - WIDTH4) // 2, (HEIGHT - HEIGHT8) // 2))
        self.screen.blit(self.settings_text, ((WIDTH - WIDTH4) // 2, (HEIGHT + 100) // 2))

    def check_m_on_play(self, mouse, click, key):
        """
        checks if mouse on the play button
        """
        pg.draw.rect(self.screen, COLOR_UNPRESSED_MENU,
                     ((WIDTH - WIDTH4) // 2, (HEIGHT - HEIGHT8) // 2, WIDTH4, HEIGHT8))

        if ((WIDTH - WIDTH4) // 2 <= mouse[0] <= ((WIDTH - WIDTH4) // 2 + WIDTH4)) \
                and ((HEIGHT - HEIGHT8) // 2 <= mouse[1] <= ((HEIGHT - HEIGHT8) // 2 + HEIGHT8)):
            pg.draw.rect(self.screen, COLOR_PRESSED_MENU,
                                 ((WIDTH - WIDTH4) // 2, (HEIGHT - HEIGHT8) // 2, WIDTH4, HEIGHT8))
            if click[0] == 1:
                self.game.start_game()
        elif key[pg.K_SPACE]:
            self.game.start_game()

    def check_m_on_settings(self, mouse, click, key):
        """
        checks if mouse on the settings button
        """
        pg.draw.rect(self.screen, COLOR_UNPRESSED_MENU,
                     ((WIDTH - WIDTH4) // 2, (HEIGHT + 100) // 2, WIDTH4, HEIGHT8))

        if ((WIDTH - WIDTH4) // 2 <= mouse[0] <= ((WIDTH - WIDTH4) // 2 + WIDTH4)) \
                and ((HEIGHT + 100) // 2 <= mouse[1] <= ((HEIGHT + 100) // 2 + 100)):
            pg.draw.rect(self.screen, COLOR_PRESSED_MENU,
                                 ((WIDTH - WIDTH4) // 2, (HEIGHT + 100) // 2, WIDTH4, HEIGHT8))
            if click[0] == 1:
                self.settings.display_settings()
        elif key[pg.K_k]:
            self.settings.display_settings()

    def update(self):
        """
        method updating menu icons and text
        """
        self.screen.fill(COLOR_MENU)

        key = pg.key.get_pressed()
        mouse = pg.mouse.get_pos()  # using coordinates of mouse of player
        click = pg.mouse.get_pressed()  # using click check of mouse of player

        self.check_m_on_play(mouse, click, key)
        self.check_m_on_settings(mouse, click, key)

        self.draw_buttons(self.configs_menu)

        quit()
