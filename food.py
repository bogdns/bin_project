import pygame
from random import randrange
from snake import *
class Food:
    def __init__(self, width):
        self.foodOnMap = 0
        self.coordfoodX = randrange(0, width)
        self.coordfoodY = randrange(0, width)

    def food_eated(self):
        if S == self.coordfoodX and y_coord == self.coordfoodY:
            length += 1
            self.foodOnMap = 0
