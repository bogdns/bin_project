from collections import deque


class Snake:
    class Snake:
        def __init__(self):
            """
            direction: top - 1, down - 2, right - 3, left - 4
            """
            self.direction = 1
            self.pos = deque()  # positions of the snake(what cells is it on)
            self.pos.append((ROWS // 2, ROWS // 2))  # places head of the snake in the center

        def draw_green_cell(self, cords):
            pass

        def draw_snake(self):
            pass

        def update(self):
            """
            moves snake
            """
