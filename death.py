from food import *
import time


class Death:
    def __init__(self, window):
        self.window = window
        self.font = pg.font.SysFont(*FONT_DEATH)

    def death_elements(self, score):
        self.window.fill(COLOR_GAME_OVER_BACK)
        result_text = self.font.render(f"Your score {score}", 1, COLOR_GAME_OVER)
        self.window.blit(result_text, (WIDTH // 8, HEIGHT // 4))
        death_text = self.font.render("Game over", 1, COLOR_GAME_OVER)
        self.window.blit(death_text, (WIDTH // 8, WIDTH // 8))

    def death_check(self, pos):
        if not (0 <= pos[-1][0] < ROWS and 0 <= pos[-1][1] < ROWS) or pos.count(pos[-1]) > 1:
            return True
        return False

    def display_death(self, score):
        while True:
            CLOCK.tick(24)
            self.death_elements(score)
            key = pg.key.get_pressed()
            if key[pg.K_SPACE]:
                time.sleep(0.4)
                break
            quit()
            pg.display.update()
