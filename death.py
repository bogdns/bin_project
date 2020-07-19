from food import *
import time


class Death:
    def __init__(self, window):
        self.screen = window
        self.font = pg.font.SysFont(*FONT_DEATH)

    def death_elements(self, score):
        if not ROFL_MODE:
            self.screen.fill(COLOR_GAME_OVER_BACK)
        result_text = self.font.render(f"Your score {score}", 1, COLOR_GAME_OVER)
        self.screen.blit(result_text, (WIDTH // 20, HEIGHT // 3))
        death_text = self.font.render("Game over", 1, COLOR_GAME_OVER)
        self.screen.blit(death_text, (WIDTH // 20, WIDTH // 4))

    def death_check(self, pos):
        if not (0 <= pos[-1][0] < ROWS and 0 <= pos[-1][1] < ROWS) or pos.count(pos[-1]) > 1:
            return True
        return False

    def display_death(self, score):
        self.config = choice(DEFEAT_SOUNDS)
        self.defeat_sounds = pg.mixer.Sound(self.config[0])
        self.defeat_sounds.set_volume(self.config[1])
        self.defeat_sounds.play()
        if ROFL_MODE:
            self.defeat_photo = pg.transform.scale(
                pg.image.load(choice(DEFEAT_PHOTOS)).convert(),
                (WIDTH, HEIGHT))

        time.sleep(0.3)
        while True:
            CLOCK.tick(24)
            if ROFL_MODE:
                self.screen.blit(self.defeat_photo, (0, 0))
            self.death_elements(score)
            key = pg.key.get_pressed()
            if key[pg.K_SPACE]:
                time.sleep(0.4)
                break
            quit()
            pg.display.update()
