import pygame

# создание окна
width = 900
height = 900
window = pygame.display.set_mode((width, height))  # окно самого pygame
pygame.init()  # инициализация библиотеки
pygame.display.set_caption("Name of game")  # название игры на окне
icon = pygame.image.load("a2f3b680ae0498546d10a563c4a1e18d.png")  # загрузка лого игры
pygame.display.set_icon(icon)  # отображение лого игры

# создание игрока
playerImg = pygame.image.load("a2f3b680ae0498546d10a563c4a1e18d.png")
playerX = 0
playerY = 0
speed = 10

def player(x, y):
    window.blit(playerImg, (x, y))  # обьединение картинки и ее расположение на экране


def run_game():
    global playerY, playerX , speed
    while True:
        for event in pygame.event.get():  # проверка действий в pygame
            if event.type == pygame.QUIT:  # если нажата кнопка X (quit)
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()  # запоминает какая кнопка нажата
        if key[pygame.K_DOWN]:  # если нажата кнопка вниз
            playerY += speed
        if key[pygame.K_UP]:  # если нажата кнопка вверх
            playerY -= speed
        if key[pygame.K_LEFT]:  # если нажата кнопка влево
            playerX -= speed
        if key[pygame.K_RIGHT]:  # если нажата кнопка вправо
            playerX += speed
        playerY += speed
        playerX += speed
        if (playerY or playerX) > 900 or (playerY or playerX) < 0:
            speed = -speed
        elif speed < 0:
            speed = -speed
        window.fill(pygame.Color("red"))  # заполнение всего окна красным цветом
        player(playerX, playerY)
        pygame.display.update()  # обновление дисплея


run_game()
