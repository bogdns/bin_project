from setting import *


class Settings:
    def __init__(self, window):
        self.window = window
        self.font = pg.font.SysFont(*FONT_SETTINGS)

    def change_settings(self, mouse, click):

    def settings_elements(self):
        self.window.fill(COLOR_MENU)

        resolution_text = self.font.render("Resolution is " + "{}".format(RESOLUTION), 1, COLOR_GAME_OVER)
        self.window.blit(resolution_text, (WIDTH // 8, HEIGHT // 8))
        text_size_text = self.font.render("Text size is " + "{}".format(TEXT_SIZE), 1, COLOR_GAME_OVER)
        self.window.blit(text_size_text, (WIDTH // 8, HEIGHT // 8 + 20))
        rows_text = self.font.render("Rows in matrix is " + "{}".format(ROWS), 1, COLOR_GAME_OVER)
        self.window.blit(rows_text, (WIDTH // 8, HEIGHT // 8 + 40))

    def display_settings(self):
        while True:
            CLOCK.tick(24)
            self.settings_elements()
            key = pg.key.get_pressed()
            if key[pg.K_ESCAPE]:
                break
            quit()
            pg.display.update()
