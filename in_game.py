from snake import *
from death import *


class Game:
    def __init__(self, window):
        self.screen = window
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        self.death = Death(self.screen)

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

    def death_check(self, head_pos):
        if not (0 <= head_pos[0] < ROWS and 0 <= head_pos[1] < ROWS):
            return True
        return False

    def start_game(self):
        """
        launch game method
        """
        self.snake.spawn()
        self.food.score = 0
        while True:
            CLOCK.tick(FPS)
            self.screen.fill(COLOR_GROUND)
            self.draw_matrix()
            self.snake.update(self.food.ate)
            self.food.update(self.snake.pos)
            if self.death_check(self.snake.pos[-1]):
                self.status = True
                break
            # elif victory_check():
            #   self.status = False
            #   break
            quit()
            pg.display.update()
        if self.status:
            while True:
                CLOCK.tick(24)
                self.death.display_death(self.food.score)
                key = pg.key.get_pressed()
                if key[pg.K_SPACE]:
                    break
                quit()
                pg.display.update()
        # else:
        #   window.display_victory()
