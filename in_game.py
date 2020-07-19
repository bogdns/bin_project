from snake import *
from death import *


class Game:
    def __init__(self, window):
        self.screen = window
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        self.death = Death(self.screen)
        self.result_text = pg.font.SysFont(*FONT_VICTORY).render("VICTORY! BEER?", 1, COLOR_VICTORY)

    def draw_matrix(self):
        """
        method for making matrix
        """
        matrix_x = 0
        matrix_y = 0
        for i in range(ROWS):
            matrix_x += DIST_BETWEEN
            matrix_y += DIST_BETWEEN
            pg.draw.line(self.screen, COLOR_LINE, (matrix_x, 0), (matrix_y, HEIGHT))
            pg.draw.line(self.screen, COLOR_LINE, (0, matrix_y), (WIDTH, matrix_y))

    def victory_check(self):
        if len(self.snake.pos) == ROWS ** 2:
            return True
        return False

    def display_victory(self):
        """
        open victory screen
        """
        self.config = choice(VICTORY_SOUNDS)
        self.victory_sounds = pg.mixer.Sound(self.config[0])
        self.victory_sounds.set_volume(self.config[1])
        self.victory_sounds.play()
        self.victory_photo = pg.transform.scale(
            pg.image.load(choice(VICTORY_PHOTOS)).convert(),
            (WIDTH, HEIGHT))

        for i in range(ROWS ** 2):
            CLOCK.tick(ROWS ** 2 // 5)
            self.snake.pos.popleft()
            self.screen.fill(COLOR_GROUND)
            self.draw_matrix()
            self.snake.end_game_snake_update()
            quit()
            pg.display.update()

        while True:
            CLOCK.tick(10)

            self.screen.blit(self.victory_photo, (0, 0))

            key = pg.key.get_pressed()

            if key[pg.K_SPACE]:
                time.sleep(0.3)
                break

            quit()

            pg.display.update()

    def start_game(self):
        """
        launch game method
        """
        self.snake.spawn()
        self.food.score = 0
        self.food.calculate_pos(self.snake.pos)
        while True:
            CLOCK.tick(FPS)

            self.screen.fill(COLOR_GROUND)
            self.draw_matrix()
            self.snake.update(self.food.ate)
            self.food.update(self.snake.pos)

            if self.death.death_check(self.snake.pos):
                self.status = True
                break
            elif self.victory_check():
                self.status = False
                break

            quit()

            pg.display.update()

        if self.status:
            self.death.display_death(self.food.score)
        else:
            self.display_victory()
