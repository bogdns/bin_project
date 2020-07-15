import pygame

pygame.init()
window = pygame.display.set_mode((1200, 1040))
pygame.display.set_caption("Snail the game")

x = 50
y = 60
width = 50
height = 60
speed = 5

run = True

while run:
    pygame.time.delay(500)