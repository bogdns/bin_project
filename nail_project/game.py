Куда летим пацаны
Какой кортеж
Улетаю























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
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed


    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
