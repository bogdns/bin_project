from food import *


class Death:
    def __init__(self, window):
        self.window = window
        self.font = pg.font.SysFont(*FONT_DEATH)

    def display_death(self, score):
        self.window.fill(COLOR_GAME_OVER_BACK)
        result_text = self.font.render(f"Your score {score}", 1, COLOR_GAME_OVER)
        self.window.blit(result_text, (50, 100))
        death_text = self.font.render("Game over", 1, COLOR_GAME_OVER)
        self.window.blit(death_text, (50, 50))
