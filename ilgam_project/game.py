import pygame

width = 600
height = 600
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snail the game")
run = True
rows = 20
while run:
    pygame.time.delay(50)
    lengBtwn = width // rows
    window.fill((0, 0, 0))
    x = 0
    y = 0
    for i in range(rows):
        x += lengBtwn
        y += lengBtwn
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, height))
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
