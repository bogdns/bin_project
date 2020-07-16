from collections import deque


class Snake:
    def __init__(self):
        """
        direction: top - 1, down - 2, right - 3, left - 4
        """
        self.direction = 1
        self.pos = deque()  # positions of the snake(what cells is it on)

    def spawn(self, size):
        """
        spawns snake in the centre of the map
        size - size of the matrix. gets cortege with quantity of cells
        """
        self.pos.append((size // 2, size // 2))  # places head of the snake in the centre
        # TO DO

    def update(self):
        """
        moves snake
        """

