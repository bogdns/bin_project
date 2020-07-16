from collections import deque
import pygame


class Snake:
    def __init__(self, distanceBetween, width, window):
        self.display = window
        self.x_coordS = 0  # X coordinates of snake
        self.y_coordS = 0  # Y coordinates of snake
        self.distanceBetween = distanceBetween  # distance between horizontals line / verticals line
        # self.pos = deque()  # positions of the snake(what cells is it on)
        self.directionX = 1  # direction on X
        self.directionY = 0  # direction on Y

    def spawn(self, width):
        # self.pos.append((width // 2, width // 2))  # places head of the snake in the centre
        pass

    def move(self):
        key = pygame.key.get_pressed()  # return button which is pressed
        if key[pygame.K_RIGHT]:
            self.directionX = 1  # change direction on x (0 - not change position; 1 - right; -1 - left)
            self.directionY = 0  # change direction on y (0 - not change position; 1 - down; -1 - up)
        if key[pygame.K_LEFT]:
            self.directionX = -1
            self.directionY = 0
        if key[pygame.K_UP]:
            self.directionY = -1
            self.directionX = 0
        if key[pygame.K_DOWN]:
            self.directionY = 1
            self.directionX = 0

        self.x_coordS = self.x_coordS + self.directionX * self.distanceBetween  # directional movement on X
        self.y_coordS = self.y_coordS + self.directionY * self.distanceBetween  # directional movement on Y

    def draw(self):
        pygame.draw.rect(self.display, (0, 255, 0),
                         (
                             self.x_coordS, self.y_coordS, self.distanceBetween,
                             self.distanceBetween))  # draw rectangle of snake
