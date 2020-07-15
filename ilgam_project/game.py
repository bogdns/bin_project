import pygame
from random import randrange

width = 600
height = 600
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snail the game")
run = True
rows = 20
x_coord = 0
y_coord = 0
lengBtwn = width // rows
x = 0
y = 0
food = 0
dirn_x = 1
dirn_y = 1
length = 1
while run:
    pygame.time.delay(200)
    window.fill((0, 0, 0))
    if food == 0:
        x_coordf = (randrange(0, height) // lengBtwn) * lengBtwn
        y_coordf = (randrange(0, height) // lengBtwn) * lengBtwn
        # pygame.draw.rect(window, (0, 255, 0), (x_coord - (dirn_x*lengBtwn), y_coord - (dirn_y*lengBtwn), lengBtwn, lengBtwn))
        pygame.draw.rect(window, (255, 0, 0), (x_coordf, y_coordf, lengBtwn, lengBtwn))
        food = 1
    pygame.draw.rect(window, (255, 0, 0), (x_coordf, y_coordf, lengBtwn, lengBtwn))
    pygame.draw.rect(window, (0, 255, 0), (x_coord, y_coord, lengBtwn, lengBtwn))
    for i in range(rows):
        x += lengBtwn
        y += lengBtwn
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, height))
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        dirn_x = 1
        dirn_y = 0
    if key[pygame.K_LEFT]:
        dirn_x = -1
        dirn_y = 0
    if key[pygame.K_UP]:
        dirn_y = -1
        dirn_x = 0
    if key[pygame.K_DOWN]:
        dirn_y = 1
        dirn_x = 0

    x_coord = x_coord + dirn_x * lengBtwn
    y_coord = y_coord + dirn_y * lengBtwn

    if x_coord == x_coordf and y_coord == y_coordf:
        length += 1
        food = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x = 0
    y = 0
    pygame.display.update()

pygame.quit()
