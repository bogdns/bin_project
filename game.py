from collections import deque
from random import choice
from time import sleep
from configparser import ConfigParser
import pygame as pg

pg.init()

# configs
config = ConfigParser()
config.read("config.ini")
LENGTH = int(config.get("game", "resolution"))
ROWS = int(config.get("game", "rows"))
FPS = int(config.get("game", "fps"))
TEXT_SIZE = LENGTH // 15
COLOR_SNAKE = eval(config.get("color", "color_snake"))
COLOR_GROUND = eval(config.get("color", "color_ground"))
COLOR_LINE = eval(config.get("color", "color_line"))
COLOR_FOOD = eval(config.get("color", "color_food"))
COLOR_MENU = eval(config.get("color", "color_menu"))
COLOR_PLAY = eval(config.get("color", "color_play"))
COLOR_SETTINGS = eval(config.get("color", "color_settings"))
COLOR_SNAKE_GAME = eval(config.get("color", "color_snake_game"))
COLOR_UNPRESSED_MENU = eval(config.get("color", "color_unpressed_menu"))
COLOR_PRESSED_MENU = eval(config.get("color", "color_pressed_menu"))
COLOR_GAME_OVER = eval(config.get("color", "color_game_over"))
COLOR_GAME_OVER_BACK = eval(config.get("color", "color_game_over_back"))
COLOR_VICTORY = eval(config.get("color", "color_victory"))
COLOR_TEXT_SETTINGS = eval(config.get("color", "color_text_settings"))
COLOR_TEXT_SETTINGS_S = eval(config.get("color", "color_text_settings_s"))
FONT_DEATH = eval(config.get("text", "font_death"))
FONT_MENU = eval(config.get("text", "font_menu"))
FONT_VICTORY = eval(config.get("text", "font_victory"))
FONT_SETTINGS = eval(config.get("text", "font_settings"))
DEFEAT_SOUNDS = eval(config.get("sound", "defeat_sounds"))
VICTORY_SOUNDS = eval(config.get("sound", "victory_sounds"))
EAT_FOOD = pg.mixer.Sound('sounds/eat_food.ogg')
EAT_FOOD.set_volume(1)

# optimise
LENGTH4 = LENGTH // 4
LENGTH8 = LENGTH // 8
DIST_BETWEEN = LENGTH // ROWS
CLOCK = pg.time.Clock()


class Window:
    def __init__(self):
        pg.display.set_caption("Snake the game")  # article on the window
        icon = pg.image.load("snake.png")  # set icon of the app
        pg.display.set_icon(icon)  # display icon
        self.window = pg.display.set_mode((LENGTH, LENGTH))  # init window
        self.in_menu = Menu(self.window)

    def update(self):
        """
        opens menu
        """
        while True:
            CLOCK.tick(24)
            if self.in_menu.update():
                break
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit(0)
            pg.display.update()


class Menu:
    def __init__(self, wn):
        self.screen = wn
        self.game = Game(self.screen)
        self.settings = Settings(self.screen)

        self.font = pg.font.SysFont(*FONT_MENU)
        self.main_text = self.font.render("Snake game", 1, COLOR_SNAKE_GAME)
        self.play_text = self.font.render("Play", 1, COLOR_PLAY)
        self.settings_text = self.font.render("Settings", 1, COLOR_SETTINGS)
        self.configs_menu = (self.screen, COLOR_UNPRESSED_MENU,
                             ((LENGTH - LENGTH4) // 2, (LENGTH - LENGTH8) // 2, LENGTH4, LENGTH8))

    def draw_buttons(self):
        """
        shows buttons on the menu screen
        """
        self.screen.blit(self.main_text, ((LENGTH - LENGTH // 2.35) // 2, LENGTH4))
        self.screen.blit(self.play_text, ((LENGTH - LENGTH4) // 2, (LENGTH - LENGTH8) // 2))
        self.screen.blit(self.settings_text, ((LENGTH - LENGTH4) // 2, (LENGTH + 100) // 2))

    def check_m_on_play(self):
        """
        checks if mouse on the play button
        """
        pg.draw.rect(self.screen, COLOR_UNPRESSED_MENU,
                     ((LENGTH - LENGTH4) // 2, (LENGTH - LENGTH8) // 2, LENGTH4, LENGTH8))

        if ((LENGTH - LENGTH4) // 2 <= self.mouse[0] <= ((LENGTH - LENGTH4) // 2 + LENGTH4)) \
                and ((LENGTH - LENGTH8) // 2 <= self.mouse[1] <= ((LENGTH - LENGTH8) // 2 + LENGTH8)):
            pg.draw.rect(self.screen, COLOR_PRESSED_MENU,
                         ((LENGTH - LENGTH4) // 2, (LENGTH - LENGTH8) // 2, LENGTH4, LENGTH8))
            if self.click[0] == 1:
                self.game.start_game()
        elif self.key[pg.K_SPACE]:
            self.game.start_game()

    def check_m_on_settings(self):
        """
        checks if mouse on the settings button
        """
        pg.draw.rect(self.screen, COLOR_UNPRESSED_MENU,
                     ((LENGTH - LENGTH4) // 2, (LENGTH + 100) // 2, LENGTH4, LENGTH8))

        if ((LENGTH - LENGTH4) // 2 <= self.mouse[0] <= ((LENGTH - LENGTH4) // 2 + LENGTH4)) \
                and ((LENGTH + 100) // 2 <= self.mouse[1] <= ((LENGTH + 100) // 2 + 100)):
            pg.draw.rect(self.screen, COLOR_PRESSED_MENU,
                         ((LENGTH - LENGTH4) // 2, (LENGTH + 100) // 2, LENGTH4, LENGTH8))
            if self.click[0] == 1:
                if self.settings.display_settings():
                    return True
        elif self.key[pg.K_k]:
            self.settings.display_settings()
        return False

    def update(self):
        """
        shows menu icons, text and check buttons
        """
        self.screen.fill(COLOR_MENU)

        self.key = pg.key.get_pressed()
        self.mouse = pg.mouse.get_pos()  # using coordinates of mouse of player
        self.click = pg.mouse.get_pressed()  # using click check of mouse of player

        self.check_m_on_play()
        if self.check_m_on_settings():
            return True
        self.draw_buttons()

        quit_game()
        return False


class Settings:
    def __init__(self, wn):
        self.screen = wn
        self.font = pg.font.SysFont(*FONT_SETTINGS)
        self.font_mark = pg.font.SysFont('ubuntu', TEXT_SIZE // 2)

        self.c_r = False
        self.c_rw = False
        self.c_f = False

        self.res = str(LENGTH)
        self.rows = str(ROWS)
        self.fps = str(FPS)

    def check_m_on_back(self):
        if 0 <= self.mouse[0] <= LENGTH // 5.5 \
                and 0 <= self.mouse[1] <= LENGTH // 14:
            pg.draw.rect(self.screen, COLOR_PRESSED_MENU,
                         (0, 0, LENGTH // 5.5, LENGTH // 14))
            if self.click[0] == 1:
                self.res = str(LENGTH)
                self.rows = str(ROWS)
                self.fps = str(FPS)
                return True
        elif self.key[pg.K_ESCAPE]:
            self.res = str(LENGTH)
            self.rows = str(ROWS)
            self.fps = str(FPS)
            return True
        else:
            pg.draw.rect(self.screen, COLOR_UNPRESSED_MENU,
                         (0, 0, LENGTH // 5.5, LENGTH // 14))

    def check_res(self):
        if LENGTH8 <= self.mouse[0] <= LENGTH8 + LENGTH // 1.5 \
                and LENGTH8 <= self.mouse[1] <= LENGTH8 + TEXT_SIZE:
            if self.click[0] == 1:
                self.c_r = True

    def check_row(self):
        if LENGTH8 <= self.mouse[0] <= LENGTH8 + LENGTH // 1.5 \
                and LENGTH4 <= self.mouse[1] <= LENGTH4 + TEXT_SIZE:
            if self.click[0] == 1:
                self.c_rw = True

    def check_fps(self):
        if LENGTH8 <= self.mouse[0] <= LENGTH8 + LENGTH // 1.5 \
                and LENGTH // 3 <= self.mouse[1] <= LENGTH // 3 + TEXT_SIZE:
            if self.click[0] == 1:
                self.c_f = True

    def check_int(self, num):
        try:
            int(num)
            return True
        except:
            return False

    def check_apply(self):
        if LENGTH // 3.1 <= self.mouse[0] <= LENGTH // 3 + LENGTH // 4.5 and LENGTH * 0.9 <= \
                self.mouse[1] <= LENGTH * 0.9 + TEXT_SIZE:
            pg.draw.rect(self.screen, COLOR_PRESSED_MENU,
                         (LENGTH // 3.1, LENGTH * 0.9, LENGTH // 4.5, TEXT_SIZE))
            if self.click[0] == 1:
                return True
        else:
            pg.draw.rect(self.screen, COLOR_UNPRESSED_MENU,
                         (LENGTH // 3.1, LENGTH * 0.9, LENGTH // 4.5, TEXT_SIZE))
        return False

    def settings_elements(self):
        """
        display settings elements
        """
        self.screen.blit(self.font.render("BACK", 1, COLOR_TEXT_SETTINGS), (0, 0))
        self.screen.blit(self.font.render(f"Resolution: {self.res}", 1, COLOR_TEXT_SETTINGS),
                         (LENGTH8, LENGTH8))
        self.screen.blit(self.font.render(f"Rows: {self.rows}", 1, COLOR_TEXT_SETTINGS),
                         (LENGTH8, LENGTH4))
        self.screen.blit(self.font_mark.render("PRESS ENTER TO STOP INPUT", 1, COLOR_TEXT_SETTINGS_S),
                         (LENGTH8, LENGTH // 5))
        self.screen.blit(self.font.render(f"APPLY", 1, COLOR_TEXT_SETTINGS),
                         (LENGTH // 3, LENGTH * 0.9))
        self.screen.blit(self.font.render(f"SPEED(FPS): {self.fps}", 1, COLOR_TEXT_SETTINGS),
                         (LENGTH8, LENGTH // 3))

    def display_settings(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit(0)
                if event.type == pg.KEYDOWN:
                    if self.c_r:
                        if event.key == pg.K_BACKSPACE:
                            self.res = self.res[:-1]
                        elif event.key == pg.K_RETURN:
                            if self.check_int(self.res):
                                self.c_r = False
                            else:
                                self.res = "WRITE NUMBER"
                        else:
                            self.res += event.unicode

                    if self.c_rw:
                        if event.key == pg.K_BACKSPACE:
                            self.rows = self.rows[:-1]
                        elif event.key == pg.K_RETURN:
                            if self.check_int(self.rows):
                                self.c_rw = False
                            else:
                                self.rows = "WRITE NUMBER"
                        else:
                            self.rows += event.unicode

                    if self.c_f:
                        if event.key == pg.K_BACKSPACE:
                            self.fps = self.fps[:-1]
                        elif event.key == pg.K_RETURN:
                            if self.check_int(self.fps):
                                self.c_f = False
                            else:
                                self.fps = "WRITE NUMBER"
                        else:
                            self.fps += event.unicode

            CLOCK.tick(24)
            self.screen.fill(COLOR_MENU)

            self.key = pg.key.get_pressed()
            self.mouse = pg.mouse.get_pos()  # using coordinates of mouse of a player
            self.click = pg.mouse.get_pressed()

            if self.check_m_on_back():
                return False
            if self.check_apply():
                return True

            self.check_res()
            self.check_row()
            self.check_fps()

            self.settings_elements()

            pg.display.update()


class Game:
    def __init__(self, wn):
        self.screen = wn
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)
        self.death = Death(self.screen)
        self.result_text = pg.font.SysFont(*FONT_VICTORY).render("VICTORY! BEER?", 1, COLOR_VICTORY)

    def draw_matrix(self):
        """
        draws lines in game
        """
        for i in range(ROWS - 1):
            t = DIST_BETWEEN * (i + 1)
            pg.draw.line(self.screen, COLOR_LINE, (t, 0), (t, LENGTH))
            pg.draw.line(self.screen, COLOR_LINE, (0, t), (LENGTH, t))

    def victory_check(self):
        """
        checks if snake won
        """
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

        for i in range(ROWS ** 2):
            CLOCK.tick(ROWS ** 2 // 5)
            self.snake.pos.popleft()
            self.screen.fill(COLOR_GROUND)
            self.draw_matrix()
            self.snake.end_game_snake_update()
            quit_game()
            pg.display.update()

        while True:
            CLOCK.tick(10)

            self.screen.fill(COLOR_GROUND)
            self.screen.blit(self.result_text, (LENGTH // 20, LENGTH // 4))

            key = pg.key.get_pressed()

            if key[pg.K_SPACE]:
                sleep(0.3)
                break

            quit_game()

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

            quit_game()

            pg.display.update()

        if self.status:
            self.death.display_death(self.food.score)
        else:
            self.display_victory()


class Snake:
    def __init__(self, wn):
        self.pos = deque()  # positions of the snake(what cells is it on)
        self.spawn()
        self.window = wn
        self.direction_x = 0
        self.direction_y = -1
        self.tail = self.pos[0]

    def spawn(self):
        self.direction_x = 0
        self.direction_y = -1
        self.pos.clear()
        self.pos.append((ROWS // 2, ROWS // 2))  # places head of the snake in the center

    def draw_green_cell(self, cords):
        pg.draw.rect(self.window, COLOR_SNAKE, (*cords, DIST_BETWEEN, DIST_BETWEEN))

    def update(self, ate):
        key = pg.key.get_pressed()

        if key[pg.K_RIGHT] and self.direction_x != -1:
            self.direction_x = 1
            self.direction_y = 0
        elif key[pg.K_LEFT] and self.direction_x != 1:
            self.direction_x = -1
            self.direction_y = 0
        elif key[pg.K_UP] and self.direction_y != 1:
            self.direction_y = -1
            self.direction_x = 0
        elif key[pg.K_DOWN] and self.direction_y != -1:
            self.direction_y = 1
            self.direction_x = 0

        if ate:
            self.pos.appendleft(self.tail)

        self.pos.append((self.pos[-1][0] + self.direction_x,
                         self.pos[-1][1] + self.direction_y))

        self.tail = self.pos.popleft()

        for cords in self.pos:
            x = cords[0]
            y = cords[1]
            self.draw_green_cell((x * DIST_BETWEEN, y * DIST_BETWEEN))

    def end_game_snake_update(self):
        """
        snake update after victory
        """
        for cords in self.pos:
            x = cords[0]
            y = cords[1]
            self.draw_green_cell((x * DIST_BETWEEN, y * DIST_BETWEEN))


class Food:
    def __init__(self, wn):
        self.pos = (0, 0)  # init pos of a food
        self.screen = wn
        self.free_cells = set()  # cells which are free to place food
        for i in range(ROWS):
            for j in range(ROWS):
                self.free_cells.add((i, j))
        self.calculate_pos([(ROWS // 2, ROWS // 2), (ROWS // 2, ROWS // 2 - 1)])
        self.ate = 0
        self.score = 0

    def calculate_pos(self, snake_pos):
        """
        calculates position of a food
        """
        if len(snake_pos) == ROWS ** 2:
            self.cords = (-2, -2)
        else:
            self.cords = choice(list(self.free_cells.difference(set(snake_pos))))  # return position. cortege

    def draw_food(self):
        """
        spawns like cells of the snake
        """
        pg.draw.rect(self.screen, COLOR_FOOD,
                     (self.cords[0] * DIST_BETWEEN,
                      self.cords[1] * DIST_BETWEEN,
                      DIST_BETWEEN,
                      DIST_BETWEEN))

    def update(self, snake_pos):
        """
        spawns food with library randint
        gets deque with positions of the snake and returns pos of the food
        """
        self.ate = 0
        if snake_pos[-1] == self.cords:  # поедание еды
            EAT_FOOD.play()
            self.calculate_pos(snake_pos)
            self.ate = 1
            self.score += 1
        self.draw_food()


class Death:
    def __init__(self, wn):
        self.screen = wn
        self.font = pg.font.SysFont(*FONT_DEATH)

    def death_elements(self, score):
        self.screen.fill(COLOR_GAME_OVER_BACK)
        self.screen.blit(self.font.render(f"Your score {score}", 1, COLOR_GAME_OVER),
                         (LENGTH // 20, LENGTH // 3))
        self.screen.blit(self.font.render("Game over", 1, COLOR_GAME_OVER),
                         (LENGTH // 20, LENGTH // 4))

    def death_check(self, pos):
        if not (0 <= pos[-1][0] < ROWS and 0 <= pos[-1][1] < ROWS) or pos.count(pos[-1]) > 1:
            return True
        return False

    def display_death(self, score):
        self.config = choice(DEFEAT_SOUNDS)
        self.defeat_sounds = pg.mixer.Sound(self.config[0])
        self.defeat_sounds.set_volume(self.config[1])
        self.defeat_sounds.play()

        sleep(0.3)
        while True:
            CLOCK.tick(24)
            self.death_elements(score)
            key = pg.key.get_pressed()
            if key[pg.K_SPACE]:
                sleep(0.4)
                break
            quit_game()
            pg.display.update()


def quit_game():
    """
    helps to quit the game
    """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)


if __name__ == "__main__":
    while True:
        window = Window()
        window.update()

        LENGTH = int(window.in_menu.settings.res)
        ROWS = int(window.in_menu.settings.rows)
        FPS = int(window.in_menu.settings.fps)
        config.set("game", "RESOLUTION", str(LENGTH))
        config.set("game", "ROWS", str(ROWS))
        with open("config.ini", "w") as fin:
            config.write(fin)
        LENGTH4 = LENGTH // 4
        LENGTH8 = LENGTH // 8
        DIST_BETWEEN = LENGTH // ROWS
        TEXT_SIZE = LENGTH // 15
        FONT_DEATH = eval(config.get("text", "font_death"))
        FONT_MENU = eval(config.get("text", "font_menu"))
        FONT_VICTORY = eval(config.get("text", "font_victory"))
        FONT_SETTINGS = eval(config.get("text", "font_settings"))
