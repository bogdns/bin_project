from setting import *


class Settings:
    def __init__(self, window):
        self.window = window
        self.font = pg.font.SysFont(*FONT_DEATH)
    # TEST
    # def settings_elements(self):
    #     self.window.fill((255, 50, 0))
    #     result_text = self.font.render(f"Your score SETTINGS", 1, COLOR_GAME_OVER)
    #     self.window.blit(result_text, (WIDTH//8, HEIGHT//4))
    #     death_text = self.font.render("Game over", 1, COLOR_GAME_OVER)
    #     self.window.blit(death_text, (WIDTH//8, HEIGHT//8))
    #
    # def display_settings(self):
    #     while True:
    #         CLOCK.tick(24)
    #         self.settings_elements()
    #         key = pg.key.get_pressed()
    #         if key[pg.K_ESCAPE]:
    #             break
    #         quit()
    #         pg.display.update()
